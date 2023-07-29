from django.db import models

# Create your models here.
class Inventory(models.Model):
  code = models.IntegerField()
  name = models.CharField(max_length=255)
  price = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField()
  deleted_at = models.DateTimeField()

  def __str__(self):
    return self.name