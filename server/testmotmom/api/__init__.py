import falcon
from falcon.http_status import HTTPStatus
from sqlalchemy.engine import create_engine

from testmotmom.models.meta import Base, DBSession
from testmotmom.api.lib.middlewares import SQLAlchemyMiddleware, HandleCORS, CheckJWT

from testmotmom.api.resources.products.routes import make_routing as product_routing
from testmotmom.api.resources.auth.routes import make_routing as auth_routing

def make_app():

    app = falcon.API(middleware=[SQLAlchemyMiddleware(), HandleCORS(), CheckJWT()])

    #add routing
    product_routing(app)
    auth_routing(app)

    configure_alchemy()

    return app
    
def configure_alchemy():
    engine = create_engine('postgresql://alimov-artyom:19252630a@localhost/test-motmom')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine