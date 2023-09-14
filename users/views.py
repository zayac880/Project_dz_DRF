from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

