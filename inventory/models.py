from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inventory(models.Model):
  code = models.IntegerField()
  name = models.CharField(max_length=255)
  price = models.IntegerField()
  desc = models.TextField(null=True, blank=True, default="")
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, related_name='%(class)s_created', on_delete=models.SET_NULL, null=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True)
  updated_by = models.ForeignKey(User, related_name='%(class)s_updated', on_delete=models.SET_NULL, null=True, blank=True)
  deleted_at = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return self.name