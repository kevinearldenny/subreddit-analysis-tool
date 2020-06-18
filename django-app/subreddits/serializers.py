from subreddits.models import Post, User, Subreddit
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name']

class SubredditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subreddit
        fields = ['name', 'url', 'category', 'in_initial_target_list']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    subreddit = serializers.PrimaryKeyRelatedField(queryset=Subreddit.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'subreddit', 'author', 'url', 'created_at', 'is_text_only', 'is_original_content', 'num_comments', 'score', 'upvote_ratio']
