from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from django.shortcuts import render

from .models import UserNet
from .serializers import GetUserNetSerializer

class GetUserNetView(RetrieveAPIView):
    """ Вывод профиля пользователя
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer

class UpdateUserNetView(UpdateAPIView):
    """ Редактирование пользователя
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer