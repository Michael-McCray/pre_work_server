from django.db import models
from quizzes.models import Question


# Create your models here.
class Taken_Test(models.Model):
	"""docstring for Taken_Quiz"""
	user_id=models.IntegerField()
	test_id=models.ForeignKey('quizzes.Test',on_delete=models.CASCADE, related_name='Taken_Test')
	questions=models.ManyToManyField('quizzes.Question',through='Score',related_name='Taken_Test')

	class Meta:
		ordering = ('id',)

class Score(models.Model):
	"""docstring for Score"""
	taken_test_id=models.ForeignKey('Taken_Test',on_delete=models.CASCADE, related_name='score')
	question_id=models.ForeignKey('quizzes.Question',on_delete=models.CASCADE, related_name='score')
	# image=models.CharField(max_length=100)
	score=models.IntegerField()
	is_correct = models.BooleanField(unique=False)

	class Meta:
		ordering = ('score',)