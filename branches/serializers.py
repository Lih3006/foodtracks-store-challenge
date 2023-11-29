from rest_framework import serializers
from .models import Branch
from operating_hours.serializers import OperatingSerializer
from operating_hours.models import Operating
from django.db import IntegrityError

class BranchSerializer(serializers.ModelSerializer):
    operating_hours = OperatingSerializer(many=True)

    class Meta:
        model = Branch
        fields = [
            "id",
            "store_name",
            "zip_code",
            "state",
            "city",
            "street",
            "number",
            "email",
            "phone",
            "company",
            "operating_hours",
        ]
        read_only_fiels = ["id", "company"]
        extra_kwargs = {"company": {"read_only": True}}

    def create(self, validated_data: dict):
        try:
            operating_hours_data = validated_data.pop("operating_hours")
            company = validated_data.pop("company")

            branch_instance = Branch.objects.create(**validated_data, company=company)
            operating_hours_instances = [
                Operating.objects.create(**data) for data in operating_hours_data
            ]
            branch_instance.operating_hours.set(operating_hours_instances)
            return branch_instance
        except IntegrityError:
            message = "You already have a branch in this address. Each branch has a unique address."
            raise serializers.ValidationError({"message": message})

    def update(self, instance: Operating, validated_data: dict) -> Operating:
        operating_hours_data = validated_data.pop("operating_hours", [])
        print('Aline', instance)
        instance = super().update(instance, validated_data)
        print('Aline1', instance)
        instance.operating_hours.all().delete()
        instance.operating_hours.set(
            Operating.objects.create(**data) for data in operating_hours_data
        )

        return instance
