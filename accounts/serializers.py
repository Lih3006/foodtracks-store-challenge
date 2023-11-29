from rest_framework import serializers
from .models import Account
from branches.models import Branch
from drf_spectacular.utils import extend_schema_serializer
from drf_spectacular.utils import OpenApiExample


@extend_schema_serializer(
    exclude_fields=('id'),
    examples=[
        OpenApiExample(
            'Create Admin user',
            summary='Create Admin user',
            description='To start, create an admin user and then log in ',
            value={"username": "Stephanie", "password": "123456", "email": "stephanie@mail.com", "phone": "015112802241", "role": "owner", "is_superuser": True},
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            'Create Regional Manager user',
            summary='Create Regional Manager user',
            description='Rote to create a Regional Manager user',
            value={
                "username": "Mary",
                "password": "123456",
                "email": "mary@mail.com",
                "phone": "015112802241",
                "branches":
                    ["{{ _.id_branch }}","{{ _.id_branch_2 }}"],
                "role": "regional_manager"
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            'Create Site Manager user',
            summary='Create Site Manager user',
            description='Rote to create Site Manager user',
            value={
                    "username": "Bia",
                    "password": "123456",
                    "email": "bia@mail.com",
                    "phone": "015112802241",
                    "branches":
                        ["{{ _.id_branch }}"],
                    "role": "site_manager"
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            'Create Employer Manager user',
            summary='Create Employer user',
            description='Rote to create a Employer user',
            value={
                    "username": "Eliot",
                    "password": "123456",
                    "email": "eliot@mail.com",
                    "phone": "015112802241",
                    "branches":
                        ["{{ _.id_branch }}"],
                    "role": "site_employer"
            },
            request_only=True,
            response_only=False,
        ),]
)
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser",
            "phone",
            "role",
            "branches",
        ]

        read_only_fiels = ["id"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"default": False},
        }

    def validate_branches(self, value):
        user_role = self.initial_data.get("role", None)
        if user_role == None:
            user_role = self.context["request"].user.role

        if user_role == "owner" and len(value) != 0:
            raise serializers.ValidationError(
                {"message": "Owner does not have branches."}
            )

        if user_role == "regional_manager" and len(value) == 0:
            raise serializers.ValidationError(
                {"message": "Regional manager must have at least one branch."}
            )

        elif user_role == "site_manager" and len(value) != 1:
            raise serializers.ValidationError(
                {"message": "Site manager must have one branch."}
            )

        elif user_role == "site_employer" and len(value) != 1:
            raise serializers.ValidationError(
                {"message": "Employer must have one branch."}
            )

        return value

    def create(self, validated_data) -> Account:
        branches_data = validated_data.pop("branches")

        if validated_data["is_superuser"]:
            account = Account.objects.create_superuser(**validated_data)
        else:
            try:
                branches_instances = [
                    Branch.objects.get(id=data) for data in branches_data
                ]
            except Branch.DoesNotExist:
                raise serializers.ValidationError({"message": "Branch does not exist."})

            account = Account.objects.create_user(**validated_data)
            account.branches.set(branches_instances)

        return account

    def update(self, instance: Account, validated_data: dict) -> Account:
        branches_data = validated_data.pop("branches")

        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        super().update(instance, validated_data)

        try:
            [Branch.objects.get(id=data) for data in branches_data]
        except Branch.DoesNotExist:
            raise serializers.ValidationError({"message": "Branch does not exist."})

        instance.branches.set(branches_data)

        return instance
