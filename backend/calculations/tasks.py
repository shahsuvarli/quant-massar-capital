from celery import shared_task
import numpy as np
import datetime
from risk.models import Portfolio, RiskMetric


@shared_task
def update_risk_metrics():
    portfolios = Portfolio.objects.all()

    for portfolio in portfolios:
        # Simulate risk calculations
        returns = np.random.randn(100)  # Fake return data for demonstration
        sharpe_ratio = np.mean(returns) / np.std(returns)
        var = np.percentile(returns, 5)  # 95% confidence VaR

        # Save risk metrics to database
        RiskMetric.objects.create(portfolio=portfolio, metric_name="Sharpe Ratio",
                                  value=sharpe_ratio, as_of_date=datetime.date.today())
        RiskMetric.objects.create(
            portfolio=portfolio, metric_name="Value-at-Risk", value=var, as_of_date=datetime.date.today())
