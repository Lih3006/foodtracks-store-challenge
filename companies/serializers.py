from rest_framework import serializers
from .models import Company
from django.db import IntegrityError


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "company_name"]
        read_only_fiels = ["id"]

    def create(self, validated_data):
        try:
            return Company.objects.create(**validated_data)
        except IntegrityError:
            message = "You already have a company. Each user can have only one company."
            raise serializers.ValidationError({"message": message})
