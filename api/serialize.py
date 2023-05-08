from api.models import Servis
from rest_framework import serializers

class ServisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servis
        fields = '__all__'