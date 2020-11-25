from board.serializers import MemberSerializer, PostSerializer, CommentSerializer
from board.models import Member, Post, Comment
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
