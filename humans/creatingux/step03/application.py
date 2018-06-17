from wsgiref.simple_server import make_server

from pyramid.config import Configurator

def main():
    config = Configurator()
    config.scan("views")
    # In newer versions of pyramid (>= 1.5) chameleon is not automatically included to the installation
    # so to avoid "ValueError: No such renderer factory .pt" you need to
    # 1) pip install pyramid_chameleon
    # 2) add the following line
    config.include('pyramid_chameleon') 
    app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
