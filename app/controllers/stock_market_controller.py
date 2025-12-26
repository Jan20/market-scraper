import json

from flask import g, request, jsonify, Blueprint

from app.entities.market import Market

stock_market_blueprint = Blueprint(name='market', import_name=__name__)


@stock_market_blueprint.route(rule='/market', methods=['POST'])
def fetch_market_constituents():
    """
    Handle POST requests to fetch market constituents.

    Expects a JSON body with a 'market' field specifying the market name.
    Validates the market, invokes the stock market service, and returns the result as JSON.
    Returns an error message if validation or processing fails.
    """
    try:
        market: str = json.loads(request.data).get('market')

        if isinstance(market, str):
            try:
                market = Market(market)
            except ValueError:
                raise ValueError(f"Unknown market: {market}")

        return g.stock_market_service.fetch_market_constituents(market=market)

    except Exception as e:
        return jsonify({'error': str(e)})
