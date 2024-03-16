from rest_framework import serializers
from django.contrib.auth.models import User
from turnos.models import Turno

class UserSerializer(serializers.ModelSerializer):
    appointments = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Turno.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'appointments']
