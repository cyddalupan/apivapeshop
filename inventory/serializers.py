from rest_framework import serializers

from apivapeshop.inventory.models import Inventory

class InventorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Inventory
    fields = ['code', 'name', 'price']
