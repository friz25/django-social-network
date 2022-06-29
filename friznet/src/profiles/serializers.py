from rest_framework import serializers
from django.shortcuts import render

from .models import UserNet

class GetUserNetSerializer(serializers.ModelSerializer):
    """ Вывод инфы о user
    """
    class Meta:
        model = UserNet
        exclude = ("password", "last_login", "is_active", "is_staff", "is_superuser")