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

    def create(self, validated_data):
        operating_hours_data = validated_data.pop("operating_hours")

        branch_instance = Branch.objects.create(**validated_data)
        print(" aline operating_hours_instances")
        operating_hours_instances = [
            Operating.objects.create(**data) for data in operating_hours_data
        ]
        print(operating_hours_instances)
        # Adicione a lista de instâncias de Operating ao campo operating_hours usando o método set()
        branch_instance.operating_hours.set(operating_hours_instances)
        return branch_instance

    # TODO vincular id da company
    # TODO verificar se a empresa existe antes de criar
