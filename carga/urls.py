from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from carga.views import UserViewSet, CicloViewSet, NaturalPersonViewSet, CursoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'ciclos', CicloViewSet)
router.register(r'naturalpersons', NaturalPersonViewSet)
router.register(r'cursos', CursoViewSet)
urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),

)
