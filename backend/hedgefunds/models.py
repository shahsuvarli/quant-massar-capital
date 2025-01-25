from django.db import models
from accounts.models import User

class HedgeFundCompany(models.Model):
    name = models.CharField(max_length=200)
    inception_date = models.DateField()
    total_aum = models.DecimalField(max_digits=20, decimal_places=2)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="managed_funds")

    def __str__(self):
        return self.name

class Fund(models.Model):
    name = models.CharField(max_length=200)
    hedge_fund_company = models.ForeignKey(HedgeFundCompany, on_delete=models.CASCADE, related_name="funds")
    inception_date = models.DateField()
    total_aum = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.hedge_fund_company.name}"

class Portfolio(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name="portfolios")
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="portfolios")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.fund.name}"
