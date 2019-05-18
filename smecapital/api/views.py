from rest_framework import generics

from Loans.models import Loans
from .serializers import LoansSerializer

# Create your views here.
class LoansAPIListView(generics.ListAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer


class LoansAPIID(generics.RetrieveAPIView):
    lookup_fields = ('pk')
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer