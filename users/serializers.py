from rest_framework import serializers
from .models import *



class ScoreSerializer(serializers.ModelSerializer):

    class Meta:

        model = Score
        fields = ('__all__')


class Taken_TestSerializer(serializers.ModelSerializer):
    Question = ScoreSerializer(many=True)


    class Meta:
        model = Taken_Test
        fields = ('__all__')


