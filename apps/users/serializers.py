from rest_framework import serializers  
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'birth_date', 'gender', 'phone', 'email', 'address', 'city', 'country')