from rest_framework import serializers
from .models import Branch
from operating_hours.serializers import OperatingSerializer
from operating_hours.models import Operating
from django.db import IntegrityError
from drf_spectacular.utils import extend_schema_serializer
from drf_spectacular.utils import OpenApiExample



@extend_schema_serializer(
    exclude_fields=('id'),
    examples=[
        OpenApiExample(
            'Create a Branch 1',
            summary='Create a Branch 1',
            description='Only admin can create a Branch, Regional and Site Manager can update',
            value={
                "store_name": "Balla Beni 2",
                "zip_code": "47167",
                "state": "North Rhine-Westphalia",
                "city": "Duisburg",
                "street": "Maria Strasse",
                "number": 20,
                "email": "ballabeni@ballabeni.com",
                "phone": "049151128022411",
                "operating_hours": 
                    [{
                        "open_hour": "07:00",
                        "close_hour": "20:00",	   
                        "wednesday": True, 
                        "friday": True,
                        "saturday": True   
                        },
                        {
                        "open_hour": "07:00",
                        "close_hour": "12:00",
                        "monday": True 
                    }]
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            'Create a Branch 2',
            summary='Create a Branch 2',
            description='Only admin can create a Branch, Regional and Site Manager can update',
            value={
                "store_name": "Balla Beni 2",
                "zip_code": "47168",
                "state": "Bayern",
                "city": "Stuttgart",
                "street": "Toni Pfülf Strasse",
                "number": 201,
                "email": "ballabeni@ballabeni.com",
                "phone": "049151128022411",
                "operating_hours":
                    [{
                        "open_hour": "07:00",
                        "close_hour": "12:00",
                        "monday": True,
                        "wednesday": True,
                        "friday": True,
                        "saturday": True
                        },
                        {
                        "open_hour": "13:00",
                        "close_hour": "20:00",
                        "monday": True
                        }]
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            'Create a Branch 3',
            summary='Create a Branch 3',
            description='Only admin can create a Branch, Regional and Site Manager can update',
            value={
                "store_name": "Balla Beni 2",
                "zip_code": "47167",
                "state": "North Rhine-Westphalia",
                "city": "Köln",
                "street": "Maria Strasse",
                "number": 20,
                "email": "ballabeni@ballabeni.com",
                "phone": "049151128022411",
                "operating_hours":
                [{
                    "open_hour": "07:00",
                    "close_hour": "20:00",
                    "monday": True,
                    "wednesday": True,
                    "friday": True
                    },
                    {
                    "open_hour": "07:00",
                    "close_hour": "12:00",
                    "monday": True              
                }]
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            'Create a Branch 4',
            summary='Create a Branch 4',
            description='Only admin can create a Branch, Regional and Site Manager can update',
            value={
                "store_name": "Balla Beni 2",
                "zip_code": "47167",
                "state": "North Rhine-Westphalia",
                "city": "Düsseldorf",
                "street": "Maria Strasse",
                "number": 20,
                "email": "ballabeni@ballabeni.com",
                "phone": "049151128022411",
                "operating_hours":
                [{
                    "open_hour": "07:00",
                    "close_hour": "20:00",
                    "monday": True,
                    "wednesday": True,
                    "saturday": True
                    },
                    {
                    "open_hour": "07:00",
                    "close_hour": "12:00",
                    "monday": True
                }]
            },
            request_only=True,
            response_only=False,
        ),]
)
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
        instance = super().update(instance, validated_data)        
        instance.operating_hours.all().delete()
        instance.operating_hours.set(
            Operating.objects.create(**data) for data in operating_hours_data
        )

        return instance
