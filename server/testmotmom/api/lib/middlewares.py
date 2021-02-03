from testmotmom.models.meta import DBSession
import falcon
import jwt
from datetime import datetime
from falcon.http_status import HTTPStatus

class SQLAlchemyMiddleware(object):
    def process_response(self, req, resp, resource, is_success):
        if not is_success:
            DBSession.rollback()
        DBSession.close()

class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')

class CheckJWT(object):
    # def process_request(self, req, resp):
    #     token = req.get_header('autorization')
    #     print(token)
    #     import pdb
    #     pdb.set_trace()
        # try:
        #     decoded = jwt.decode(token, 'testmotmom', algorithms=["HS256"])
        # except Exception:
        #     import pdb
        #     pdb.set_trace()
        #     raise
    #     curent_time_ms = datetime.now().timestamp() * 1000
    #     exp = decoded['exp']
    #     if curent_time_ms > exp:
    #         print('Токен протух')
    #     else: 
    #         print('Токен еще живой')

    def process_resource(self, req, resp, resource, params):
        if getattr(resource, 'ignore_auth', None):
            return
        # token = req.get_header('autorization')
        # try:
        #     decoded = jwt.decode(token, 'testmotmom', algorithms=["HS256"])
        #     req.user_id = {"id": decoded['id']}
        # except Exception:
        #     raise falcon.HTTPForbidden('Время авторизации истекло авторизации')
