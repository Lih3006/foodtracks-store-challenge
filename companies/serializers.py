from rest_framework import serializers
from .models import Company
from accounts.serializers import AccountSerializer


class CompanySerializer(serializers.ModelSerializer):
    # owner = AccountSerializer(read_only=True)

    class Meta:
        model = Company
        fields = ["id", "company_name"]
        read_only_fiels = ["id"]

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    # TODO vincular id do user
