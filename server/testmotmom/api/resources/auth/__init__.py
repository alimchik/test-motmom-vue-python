import arrow
import json
import falcon
import bcrypt
import jwt
from datetime import datetime, timedelta

from mo.api.decorators import resource

from testmotmom import models as m
from testmotmom.api.lib.validator import validate

from .schema import auth

class Login:
    ignore_auth = True

    @falcon.before(validate(schema=auth))
    def on_post(self, req, resp):
        body = req.context['validated_params']
        email = body['email']
        password = body['password'] 
        user = m.User.objects.query().filter_by(email=email).first()
        
        if not user:
            resp.status = falcon.HTTP_401
            resp.body = json.dumps({'message': 'Пользователя с таким Email не существует'})
            return

        is_match = bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8'))

        if not is_match:
            resp.status = falcon.HTTP_401
            resp.body = json.dumps({'message': 'Неверный пароль'})
            return

        # token = jwt.encode({"id": user.id, "exp": (datetime.now() + timedelta(seconds=20)).timestamp() * 1000}, "testmotmom", algorithm="HS256").decode('utf8')
        token = jwt.encode({"id": user.id, "exp": arrow.utcnow().shift(seconds=60).timestamp}, "testmotmom", algorithm="HS256")
        resp.body = json.dumps({"token": token, "user": {"id": user.id, "email": user.email}})

class Registration:
    ignore_auth = True
    
    @falcon.before(validate(schema=auth))
    def on_post(self, req, resp):
        body = json.loads(req.stream.read())
        email = body['email']
        password = body['password']
        
        candidat = m.User.objects.query().filter_by(email=email).first()
        if candidat:
          resp.status = falcon.HTTP_401
          resp.body = json.dumps({'message': 'Пользователь с таким Email уже существует'})
          return

        hash_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
        user = m.User(email=email, password=hash_password).save()
        user.db_session.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({'message': 'Пользоватль успешно создан'})

class Refresh:
    def on_get(self, req, resp):
        token = jwt.encode({"id": req.user_id['id'], "exp": arrow.utcnow().shift(seconds=60).timestamp}, "testmotmom", algorithm="HS256")
        resp.body = json.dumps({"token": token})
