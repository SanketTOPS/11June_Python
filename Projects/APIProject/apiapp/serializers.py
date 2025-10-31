from rest_framework import serializers
from .models import *


class userserial(serializers.ModelSerializer):
    class Meta:
        model=userdata
        fields='__all__'