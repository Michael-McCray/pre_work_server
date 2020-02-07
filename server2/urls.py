from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings
# from graphene_file_upload.django import FileUploadGraphQLView

#GQL
from graphene_django.views import GraphQLView
from server2.schema import schema


urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
