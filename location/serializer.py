from rest_framework import serializers
from .models import Locations

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations  # Link the serializer to the Location model
        fields = '__all__'