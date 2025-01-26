from django.db import models
from accounts.models import User
import uuid

class PaymentInfo(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    payment_method = models.CharField(max_length=50, choices=[("CARD", "Card"), ("BANK", "Bank Transfer")])
    account_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s payment method: {self.payment_method}"
