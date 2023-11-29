from rest_framework import serializers
from .models import Company
from django.db import IntegrityError
from drf_spectacular.utils import extend_schema_serializer
from drf_spectacular.utils import OpenApiExample


@extend_schema_serializer(
    exclude_fields=('id'),
    examples=[
        OpenApiExample(
            'Create a Company with Admin user',
            summary='Create a Company with Admin user',
            description='Only admin can create, update or delete a Company, and a Admin can create only one Company',
            value={"company_name": "Balla Benni Gmbh"},
            request_only=True,
            response_only=False,
        ),])

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
