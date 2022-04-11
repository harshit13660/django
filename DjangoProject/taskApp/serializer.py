from rest_framework import serializers

from .models import userData

class userSerialiser(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ("userName","email")
