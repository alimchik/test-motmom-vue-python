from . import Login, Registration, Refresh

def make_routing(app):
    app.add_route('/api/auth/login', Login())
    app.add_route('/api/auth/registr', Registration())
    app.add_route('/api/auth/refresh', Refresh())