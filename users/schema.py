import graphene
# users/schema.py
from graphene_django import DjangoObjectType
# from graphene_file_upload.scalars import Upload 
from graphene_django.rest_framework.mutation import SerializerMutation
from .models import *
from .serializers import *


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class Taken_TestType(DjangoObjectType):
    class Meta:
        model = Taken_Test

class ScoreType(DjangoObjectType):
    class Meta:
        model = Score


# Add querys to object
class Query(graphene.ObjectType):

    # Taken_Quiz
    taken_test = graphene.Field(Taken_TestType,
                              id=graphene.Int())
    
    all_taken_tests = graphene.List(Taken_TestType)

    # Skill
    score = graphene.Field(ScoreType,
                              id=graphene.Int())

    all_scores = graphene.List(ScoreType)

    
     #  Resolve object list
    def resolve_all_taken_tests(self, info, **kwargs):
        return Taken_Test.objects.all()

    def resolve_all_scores(self, info, **kwargs):
        return Score.objects.all()


    #  Resolve single object
    def resolve_taken_test(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Taken_Test.objects.get(pk=id)

        return None

    def resolve_score(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Score.objects.get(pk=id)

        return None


# Mutations x Serializers 
class Taken_TestMutation(SerializerMutation):
    class Meta:
        serializer_class = Taken_TestSerializer

class ScoreMutation(SerializerMutation):
    class Meta:
        serializer_class = ScoreSerializer


# class UploadMutation(graphene.Mutation):
#     class Arguments:
#         file = Upload(required=True)

#     success = graphene.Boolean()

#     def mutate(self, info, file, **kwargs):
#         # do something with your file

#         return UploadMutation(success=True)

# Add mutations to object
class Mutation(graphene.ObjectType):
    create_taken_test = Taken_TestMutation.Field()
    create_score = ScoreMutation.Field()
    # upload_file = UploadMutation.Field()

