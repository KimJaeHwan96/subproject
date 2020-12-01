from django.urls import path, include
from rest_framework import routers
from .views import MemberViewSet, PostViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'member', MemberViewSet, basename='member')
router.register(r'post', PostViewSet, basename='post')
router.register(r'comment', CommentViewSet, basename='comment')
urlpatterns = [
    path('', include(router.urls)),
]
