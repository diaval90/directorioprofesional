from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Profesionales(models.Model):
	nombre 		= models.CharField(max_length = 100)
	lat			= models.CharField(max_length = 50)
	lng 		= models.CharField(max_length = 50)
	profesion	= models.CharField(max_length = 100)
	ciudad		= models.CharField(max_length = 100)

	def __unicode__ (self):
		return self.nombre
