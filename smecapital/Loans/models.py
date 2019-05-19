from decimal import Decimal

from dateutil.relativedelta import relativedelta
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
    interest_rate_per_month = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def name(self):
        name = self.borrower.name
        return name

    @property
    def APR(self):
        APR = self.interest_rate_per_month * 12
        return APR

    @property
    def monthly_repayment(self):
        monthly_interest_rate = self.interest_rate_per_month / 100
        principal = self.principal
        months = self.term_in_months
        monthly_repayment_numerator = (monthly_interest_rate * principal) * pow((1 + monthly_interest_rate), months)
        monthly_repayment_denominator = pow((1 + monthly_interest_rate), months) - 1
        monthly_repayment = monthly_repayment_numerator/monthly_repayment_denominator
        return f"{monthly_repayment:.2f}"

    @property
    def total_amount_repaid(self):
        total_amount_repaid = Decimal(self.monthly_repayment) * self.term_in_months
        return f"{total_amount_repaid:.2f}"


    @property
    def final_repayment_date(self):
        final_repayment_date = self.start_date + relativedelta(months=+(self.term_in_months - 1))
        return final_repayment_date