
from django.db import models
from django.contrib.auth.models import User

class SalesData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales_data")
    month = models.CharField(max_length=20)  # e.g., "January"
    amount = models.FloatField()  # e.g., 5000.0

    def __str__(self):
        return f"{self.user.username} - {self.month} - {self.amount}"