from django.db.models import fields
from rest_framework import serializers
from .models import Order, Receipt

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = '__all__'

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'
