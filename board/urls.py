from django.contrib import admin
from django.urls import path, include
from board import views
from rest_framework import viewsets
from rest_framework import routers
from .views import MemberViewSet, PostViewSet

router = routers.SimpleRouter()
router.register(r'member', MemberViewSet, basename='member')
router.register(r'', PostViewSet, basename='')
urlpatterns = [
    path('', include(router.urls)),
]
