from django import forms
from .models import Loans

class LoanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Loans
        exclude = ['borrower', 'approved', 'start_date']