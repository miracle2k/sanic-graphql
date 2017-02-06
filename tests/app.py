from sanic import Sanic
from sanic_graphql import GraphQLView
from .schema import Schema


def create_app(path='/graphql', **kwargs):
    app = Sanic(__name__)
    app.debug = True
    app.add_url_rule(path, view_func=GraphQLView.as_view('graphql', schema=Schema, **kwargs))
    return app


if __name__ == '__main__':
    app = create_app(graphiql=True)
    app.run()
