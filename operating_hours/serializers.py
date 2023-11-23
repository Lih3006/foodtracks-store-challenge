from rest_framework import serializers
from .models import Operating


class OperatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operating
        fields = "__all__"
