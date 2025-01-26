from django.db import models
from hedgefunds.models import Portfolio
import uuid

class RiskMetric(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="risk_metrics")
    metric_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=20, decimal_places=4)
    as_of_date = models.DateField()

    def __str__(self):
        return f"{self.metric_name} for {self.portfolio.name} on {self.as_of_date}"
