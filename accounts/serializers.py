from rest_framework import serializers
from .models import Account
from branches.models import Branch


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
        depth = 1

    def validate_branches(self, value):
        user_role = self.initial_data.get("role", None)

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
        branches_data = validated_data.pop("branches", [])

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
