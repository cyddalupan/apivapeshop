
from django.db.models import fields
from rest_framework import serializers
from .models import Inventory
 
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        # fields = ('code', 'name', 'price', 'description')