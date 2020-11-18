from django.contrib import admin
from django.urls import path, include
from board import views
from rest_framework import viewsets
from rest_framework import routers
from .views import MemberViewSet

#member_list = MemberViewSet.as_view({'get' : 'list'})
#
router = routers.SimpleRouter()
router.register(r'member', MemberViewSet, basename='member')

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    #('member/', member_list, name='member-list'),
    #path('member/<int:pk>/', member_detail, name='member-detail')
]
urlpatterns += router.urls