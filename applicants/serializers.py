from rest_framework import serializers
from .models import Candidato

class AppSerializer(serializers.ModelSerializer):
  class Meta:
    model = Candidato
    fields = '__all__'