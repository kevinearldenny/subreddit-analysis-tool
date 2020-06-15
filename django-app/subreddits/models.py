from django.db import models
from datetime import datetime
from django.utils import timezone

class Subreddit(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    url = models.CharField(max_length=500)
    category = models.CharField(max_length=100, default='General / Community')
    in_initial_target_list = models.BooleanField(default=False)
    keep_updated = models.BooleanField(default=True)
    added_to_system_date = models.DateField(default=timezone.now)

    # Returns the string representation of the model.
    def __unicode__(self):  # __unicode__ on Python 2
        return 'r/' + str(self.name)

    def __str__(self):
        return 'r/' + str(self.name)

class User(models.Model):
    name = models.CharField(max_length=250, primary_key=True)

    # Returns the string representation of the model.
    def __unicode__(self):  # __unicode__ on Python 2
        return 'u/' + str(self.name)

    def __str__(self):
        return 'u/' + str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=1000)
    subreddit = models.ForeignKey(Subreddit, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, unique=True)
    created_at = models.DateTimeField()
    is_text_only = models.BooleanField()
    is_original_content = models.BooleanField(default=False)
    num_comments = models.IntegerField(default=0)
    score = models.IntegerField(default=1)
    upvote_ratio = models.DecimalField(default=1.00, decimal_places=2, max_digits=3)
    first_synced = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


    # Returns the string representation of the model.
    def __unicode__(self):  # __unicode__ on Python 2
        return "{0}, in r/{1} by {2} on {3}".format(self.title, self.subreddit.name, self.author.name, self.created_at.strftime('%Y-%m-%d'))

    def __str__(self):
        return "{0}, in r/{1} by {2} on {3}".format(self.title, self.subreddit.name, self.author.name, self.created_at.strftime('%Y-%m-%d'))