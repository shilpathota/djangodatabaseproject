from rest_framework import serializers
from .models import DatabaseapiCacdata


class CACDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = DatabaseapiCacdata
        fields = '__all__'
