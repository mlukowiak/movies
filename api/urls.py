from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('movies', views.MoviesViewSet)
router.register('reviews', views.ReviewViewSet)
router.register('favorite', views.FavoriteViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    url('', include(router.urls))
]