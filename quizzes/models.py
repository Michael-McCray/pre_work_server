from django.db import models


# Create your models here.
class Test(models.Model):
	"""docstring for Test"""
	title=models.CharField(max_length=100)
	text =models.CharField(max_length=300)
	questions = models.ManyToManyField('Question', related_name='quiz')

	class Meta:
		ordering = ('title',)

class Question(models.Model):
	"""docstring for Question"""
	title=models.CharField(max_length=100)
	text =models.CharField(max_length=300)
	link= models.URLField(max_length=200)


	class Meta:
		ordering = ('title',)

