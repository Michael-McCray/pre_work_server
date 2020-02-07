import graphene
#Import schema
import users.schema
import quizzes.schema



class Query(
    users.schema.Query,
    quizzes.schema.Query,# Add your Query objects here
    graphene.ObjectType
):
    pass

class Mutation(
    users.schema.Mutation,
    quizzes.schema.Mutation, # Add your Mutation objects here
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)