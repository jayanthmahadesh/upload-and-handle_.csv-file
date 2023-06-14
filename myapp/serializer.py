from rest_framework import serializers
from .models import *

class sales_serializer(serializers.ModelSerializer):
    class Meta:
        model=sales
        fields ='__all__'