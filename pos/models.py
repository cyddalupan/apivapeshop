from django.db import models
from inventory.models import Inventory
from django.contrib.auth.models import User

class Receipt(models.Model):
	customer = models.CharField(max_length=255)
	total = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	created_by = models.ForeignKey(User, related_name='%(class)s_created', on_delete=models.SET_NULL, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, related_name='%(class)s_updated', on_delete=models.SET_NULL, null=True, blank=True)
	deleted_at = models.DateTimeField(null=True, blank=True, default=None)

	def __str__(self):
		return str(self.customer)

class Order(models.Model):
	receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
	item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	price = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	created_by = models.ForeignKey(User, related_name='%(class)s_created', on_delete=models.SET_NULL, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, related_name='%(class)s_updated', on_delete=models.SET_NULL, null=True, blank=True)
	deleted_at = models.DateTimeField(null=True, blank=True, default=None)

	def __str__(self):
		return str(self.created_at)

	
