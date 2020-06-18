from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets
from subreddits.serializers import UserSerializer, SubredditSerializer, PostSerializer
from subreddits.models import User, Subreddit, Post
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class SubredditViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subreddits to be viewed or edited.
    """
    queryset = Subreddit.objects.all().order_by('name')
    serializer_class = SubredditSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

class UsersList(APIView):
    def post(self, request):
        d = request.data
        j = json.loads(d)
        serializer = UserSerializer(data=j)
        if serializer.is_valid():
            serializer.save()
            msg = 'saved'
            data = serializer.validated_data
        else:
            msg = 'error'
            data = None

        df = {
            'msg': msg
        }
        if data:
            df['data'] = data
        return Response(df)