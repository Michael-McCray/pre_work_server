from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question
        fields = ('__all__')


class TestSerializer(serializers.ModelSerializer):
    Question = QuestionSerializer(many=True)


    class Meta:
        model = Test
        fields = ('__all__')


