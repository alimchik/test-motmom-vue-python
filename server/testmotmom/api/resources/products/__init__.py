import json
import falcon

from mo.api.decorators import resource

from testmotmom.api.lib.validator import validate
from testmotmom import models as m

from .schema import product


class Products:
    def on_get(self, req, resp):
        products = m.Product.objects.list(**req.params)
        resp.body = json.dumps(products['items'], default=str)
    
    @falcon.before(validate(schema=product))
    def on_post(self, req, resp):
        body = req.context['validated_params']
        product = m.Product(name=body['name'], count=body['count'], price=body['price'], date_add=body['date_add']).save()
        # # raise falcon.HTTPBadRequest(title='title', description='adasdashdahsdasdhasdad')
        product.db_session.commit()
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({'message': 'Продукт успешно добавлен'})
    
    def on_delete(self, req, resp):
        body = json.loads(req.stream.read())

        products = m.Product.objects.query().filter(m.Product.id.in_(body['data'])).all()
        for product in products:
            product.delete()

        m.Product.db_session.commit()
        
        resp.body = json.dumps({'message': 'Запись(и) успешно удалена'})

class Product:
    def on_get(self, req, resp, id):
        product = m.Product.objects.get(id)
        resp.body = json.dumps(product.jsonify(), default=str)

    @falcon.before(validate(schema=product))
    def on_patch(self, req, resp, id):
        product = m.Product.objects.get(id)
        body = req.context['validated_params']

        product.name = body['name']
        product.count = body['count']
        product.price = body['price']
        product.date_add = body['date_add']
        product.db_session.commit()

        resp.body = json.dumps(product.jsonify(), default=str)