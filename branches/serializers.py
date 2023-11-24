from rest_framework import serializers
from .models import Branch
from companies.serializers import CompanySerializer
from operating_hours.serializers import OperatingSerializer
from operating_hours.models import Operating


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
        operating_hours_data = validated_data.pop("operating_hours")

        branch_instance = Branch.objects.create(**validated_data)
        operating_hours_instances = [
            Operating.objects.create(**data) for data in operating_hours_data
        ]
        branch_instance.operating_hours.set(operating_hours_instances)
        return branch_instance

    def update(self, instance: Operating, validated_data: dict) -> Operating:
        operating_hours_data = validated_data.pop("operating_hours", [])

        instance = super().update(instance, validated_data)

        instance.operating_hours.all().delete()
        instance.operating_hours.set(
            Operating.objects.create(**data) for data in operating_hours_data
        )

        return instance
