from django.urls import path, include
from rest_framework import routers
from .views import MemberViewSet, PostViewSet

router = routers.SimpleRouter()
router.register(r'member', MemberViewSet, basename='member')
router.register(r'', PostViewSet, basename='')
urlpatterns = [
    path('', include(router.urls)),
]
