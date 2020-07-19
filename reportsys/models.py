from django.db import models


# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=20)

class Machine(models.Model):
	name = models.CharField(max_length=255)
	Description = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('Category', related_name='post')