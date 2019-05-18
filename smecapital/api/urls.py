from django.urls import path
from .views import LoansAPIListView, LoansAPIID

urlpatterns = [
    path("", LoansAPIListView.as_view(), name="results_api_list"),
    path("/<int:pk>", LoansAPIID.as_view(), name="results_api_detail"),
]
