from django.urls import path, include
from rest_framework import routers
from .views import MemberViewSet, PostViewSet
from django.contrib.auth import views as auth_views

router = routers.SimpleRouter()
router.register(r'member', MemberViewSet, basename='member')
router.register(r'', PostViewSet, basename='')
urlpatterns = [
    path('', include(router.urls)),
    #path('login/', auth_views.as_view(), name='login'),
    #path('logout/', auth_views.auth_logout.as_view())
]
