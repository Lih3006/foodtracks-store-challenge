from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser",
            "branch_state",
            "branch_city",
            "branches",
        ]
        read_only_fiels = ["id"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"default": False},
        }

    def create(self, validated_data: dict) -> Account:
        if validated_data["is_superuser"]:
            account = Account.objects.create_superuser(**validated_data)
        else:
            account = Account.objects.create_user(**validated_data)
        return account

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
            instance.save()
        return instance
