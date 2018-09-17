from django.db import models
from uuid import uuid4

# Create your models here.
class Movie(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=20)
  genre = models.TextField(max_length=15)