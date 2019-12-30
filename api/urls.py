from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('movies', views.MoviesView)

urlpatterns = [
    url('', include(router.urls))
]