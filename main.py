import logging

from flask import Flask, g

from app.controllers.stock_market_controller import stock_market_blueprint
from app.services.stock_market_service import StockMarketService


def create_app():
    app: Flask = Flask(__name__)

    app.logger.setLevel(logging.WARNING)

    @app.before_request
    def before_request() -> None:
        if 'stock_market_service' not in g:
            g.stock_market_service = StockMarketService()

    app = register_blueprints(app)

    return app


def register_blueprints(app: Flask) -> Flask:
    blueprints = [
        stock_market_blueprint,
    ]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=8080, debug=True)
