from django.urls import path

from .views import LoanListView, LoanCreateView, LoanEditView

urlpatterns =[
    path('', LoanListView.as_view(), name='loans'),
    path('create', LoanCreateView.as_view(), name='create'),
    path('edit/<int:pk>', LoanEditView.as_view(), name='edit')
]