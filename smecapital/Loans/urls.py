from django.urls import path

from .views import LoanListView, LoanCreateView

urlpatterns =[
    path('', LoanListView.as_view(), name='loans'),
    path('create', LoanCreateView.as_view(), name='create')
]