from django.db import models

# Create your models here.
class Course(models.Model):
	course = models.CharField(max_length=255)
	updated_at = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now=True)

class Description(models.Model):
	description = models.TextField(max_length=1000)
	the_course = models.OneToOneField(Course, related_name='a_course', on_delete='CASCADE')
	updated_at = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now=True)
