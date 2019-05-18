from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import User


class Loans(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    term_in_months = models.IntegerField(validators=[
            MaxValueValidator(360),
            MinValueValidator(24)
        ])
    principal = models.IntegerField(validators=[
            MaxValueValidator(1000000),
            MinValueValidator(2000)
        ])
    interest_rate_pa = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def name(self):
        name = self.borrower.name
        return name