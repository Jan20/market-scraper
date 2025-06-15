import json

from flask import g, request, jsonify, Blueprint

stock_market_blueprint = Blueprint(name='market', import_name=__name__)


@stock_market_blueprint.route(rule='/market', methods=['POST'])
def fetch_market_constituents():
    try:
        market: str = json.loads(request.data).get('market')

        if market is None:
            return jsonify({'error': 'Stock market name is expected but has not been provided'}), 400

        return g.stock_market_service.fetch_market_constituents(market=market)

    except Exception as e:
        return jsonify({'error': str(e)})
