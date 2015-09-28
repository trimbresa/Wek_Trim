from django.db import models

# Create your models here.
class AddNewUser(models.Model):
	email     = models.EmailField()
	name      = models.CharField(blank = False, max_length = 50, null = True)
	password  = models.CharField(blank = False, max_length = 250232323, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)	
	updated   = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__ (self):
		return self.email


class AddResource(models.Model):
	name     = models.CharField(blank = False, max_length = 150, null = True)
	description      = models.CharField(blank = False, max_length = 300, null = True)
	level  = models.CharField(blank = False, max_length = 999, null = True)
	url  = models.CharField(blank = False, max_length = 999, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)	
	updated   = models.DateTimeField(auto_now_add = False, auto_now = True)
                 

	def __unicode__ (self):
		return self.email