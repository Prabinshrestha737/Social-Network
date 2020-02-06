from rest_framework import serializers
from User.models import UserProfile

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'middle_name', 'last_name', 'age',
         'user_name', 'phone_number','gender','dob', 'country', 'profile_pic')

