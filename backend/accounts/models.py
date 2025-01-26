from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_trader = models.BooleanField(default=False)
    is_investor = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    account_balance = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)
    risk_tolerance = models.CharField(
        max_length=50,
        choices=[("LOW", "Low"), ("MEDIUM", "Medium"), ("HIGH", "High")],
        default="MEDIUM",
    )

    def __str__(self):
        return f"Profile of {self.user.username}"


class ApiToken(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="api_tokens")
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"API Token for {self.user.username}"


class UserActivity(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="activities")
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"
