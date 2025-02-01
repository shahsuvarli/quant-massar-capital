from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from trading.models import Trade
from hedgefunds.models import Portfolio
import numpy as np
import scipy.optimize as sco
from django.core.cache import cache


@swagger_auto_schema(method='GET', operation_description="Calculate Value at Risk for a portfolio", manual_parameters=[openapi.Parameter('portfolio_id', openapi.IN_QUERY, description="Portfolio ID", type=openapi.TYPE_STRING)])
@api_view(['GET'])
def value_at_risk(request):

    cache.set('test_key', 'Hello, Redis!', timeout=60)  # Store for 60 seconds
    print(cache.get('test_key'))  # Output: Hello, Redis!

    portfolio_id = request.query_params.get('portfolio_id')
    portfolio = Portfolio.objects.get(
       id=portfolio_id)
    if not portfolio:
        return Response({"error": "Portfolio not found"}, status=404)
    trades = Trade.objects.filter(
        portfolio=portfolio).order_by("-trade_date")

    returns = np.array([float(trade.price) for trade in trades])
    confidence_level = 0.95
    var = np.percentile(returns, 100 * (1 - confidence_level))
    return Response({"Value at Risk": var})


@swagger_auto_schema(method='GET', operation_description="Calculate Expected Shortfall for a portfolio", manual_parameters=[openapi.Parameter('portfolio_id', openapi.IN_QUERY, description="Portfolio ID", type=openapi.TYPE_STRING)])
@api_view(['GET'])
def optimize_portfolio(request):
    portfolio = Portfolio.objects.get(
        id=request.query_params.get('portfolio_id'))
    trades = Trade.objects.filter(portfolio=portfolio)

    tickers = [trade.instrument.symbol for trade in trades]
    returns = np.random.rand(len(tickers))  # Simulating random returns
    cov_matrix = np.random.rand(len(tickers), len(
        tickers))  # Simulating covariance matrix

    def portfolio_volatility(weights):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    num_assets = len(tickers)
    args = (cov_matrix,)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for asset in range(num_assets))
    result = sco.minimize(portfolio_volatility, num_assets *
                          [1./num_assets,], method='SLSQP', bounds=bounds, constraints=constraints)

    optimized_weights = result.x
    return Response({"Optimized Portfolio Weights": optimized_weights})
