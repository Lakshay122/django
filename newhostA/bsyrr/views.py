from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from bsyrr.models import User

from bsyrr.serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            User = serializer.save()
            return Response({'msg': 'registration success'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
