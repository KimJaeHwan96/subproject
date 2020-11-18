from board.serializers import MemberSerializer, PostSerializer
from rest_framework.views import APIView
from board.models import Member, Post
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class MemberViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset =  Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Member.objects.all()
        member = get_object_or_404(queryset, pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def create(self, request):
        serializer = MemberSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        member = Member.objects.all(pk=pk)
        serializer = MemberSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            member.update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
