from . import Products, Product


def make_routing(app):
    app.add_route('/api/products', Products())
    app.add_route('/api/products/{id:int}', Product())
