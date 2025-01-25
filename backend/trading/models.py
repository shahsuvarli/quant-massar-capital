from django.db import models
from hedgefunds.models import Portfolio

class Instrument(models.Model):
    SYMBOL_TYPES = [
        ('STOCK', 'Stock'),
        ('BOND', 'Bond'),
        ('FUTURE', 'Future'),
        ('OPTION', 'Option'),
        ('CRYPTO', 'Cryptocurrency'),
    ]

    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10, unique=True)
    instrument_type = models.CharField(max_length=10, choices=SYMBOL_TYPES)
    currency = models.CharField(max_length=10, default="USD")

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Trade(models.Model):
    TRADE_TYPES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="trades")
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, related_name="trades")
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
    quantity = models.DecimalField(max_digits=20, decimal_places=4)
    price = models.DecimalField(max_digits=20, decimal_places=4)
    trade_date = models.DateField()
    executed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trade_type} {self.quantity} of {self.instrument.symbol} in {self.portfolio.name}"
