from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import ListView

from .models import Loans

def create_loan():


class LoanListView(ListView):
    model = Loans

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class MyLoanMixin (object):
    permission_denied_message = "You may not modify your own loan"

    def dispatch (self, request, *args, **kwargs):
        if self.get_object().borrower == request.user:
            raise PermissionDenied(self.get_permission_denied_message())
        return super().dispatch(request, *args, **kwargs)

    def get_permission_denied_message(self):
        """
        Override this method to override the permission_denied_message attribute.
        """
        return self.permission_denied_message

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
