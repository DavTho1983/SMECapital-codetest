from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Loans
from .forms import LoanForm


class LoanListView(ListView):
    model = Loans

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class LoanCreateView(CreateView):
    model = Loans
    form_class = LoanForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.borrower = self.request.user
        return super(LoanCreateView, self).form_valid(form)


class LoanEditView(UpdateView):
    model = Loans
    form_class = LoanForm

    def get_success_url(self):
        return reverse('edit', kwargs={
            'pk': self.object.pk,
        })
