from django.shortcuts import render
from User.models import UserProfile
from rest_framework.views import APIView

# Create your views here.

class SignUpView(APIView):

    def get(self, request, format=None):
        sign_up_user = UserProfile.objects.all()
        serializer = SignUpSerializer(sign_up_user, many=True)
        return Response(serializer.data)
