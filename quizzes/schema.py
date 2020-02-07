import graphene
# users/schema.py
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from .models import *
from .serializers import *


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class TestType(DjangoObjectType):
    class Meta:
        model = Test

# Add querys to object
class Query(graphene.ObjectType):


    # Question
    question = graphene.Field(QuestionType,
                              id=graphene.Int(),
                              title=graphene.String())

    all_questions = graphene.List(QuestionType)

    # Test
    test = graphene.Field(TestType,
                              id=graphene.Int(),
                              title=graphene.String())

    all_tests = graphene.List(TestType)
    
     #  Resolve object list
    
    def resolve_all_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_all_quizzes(self, info, **kwargs):
        return Test.objects.all()

    #  Resolve single object

    def resolve_question(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Question.objects.get(pk=id)

        if title is not None:
            return Question.objects.get(title=title)

        return None

    def resolve_test(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Test.objects.get(pk=id)

        if title is not None:
            return Test.objects.get(title=title)

        return None

# Mutations x Serializers 

class QuestionMutation(SerializerMutation):
    class Meta:
        serializer_class = QuestionSerializer

class TestMutation(SerializerMutation):
    class Meta:
        serializer_class = TestSerializer

# Add mutations to object
class Mutation(graphene.ObjectType):
    create_question = QuestionMutation.Field()
    create_test = TestMutation.Field()

