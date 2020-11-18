from rest_framework import serializers
from board.models import Member, Post, GENDERS


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'gender', 'birthday', 'tel', 'created_dt', 'updated_dt']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'writer', 'created_dt', 'modify_dt']
