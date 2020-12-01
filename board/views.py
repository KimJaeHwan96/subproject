from board.serializers import MemberSerializer, PostSerializer, CommentSerializer
from board.models import Member, Post, Comment
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['^title', ]

    @action(detail=True, methods=['get'])
    def get_comment(self, request, pk=None):
        post = self.get_object()
        queryset = post.comments.all()
        filter = self.request.query_params.get('author')
        queryset = queryset.filter(author=filter)
        serializer = CommentSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, ]
    ordering_fields = ['id', 'post', 'author']


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [rest_framework.DjangoFilterBackend, ]
    filterset_fields = ['id', 'name', 'gender', 'birthday', 'tel']
