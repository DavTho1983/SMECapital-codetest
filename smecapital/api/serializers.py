from rest_framework import serializers

from Loans.models import Loans


class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'