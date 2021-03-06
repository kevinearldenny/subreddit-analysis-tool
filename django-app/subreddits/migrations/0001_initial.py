# Generated by Django 3.0.7 on 2020-06-12 20:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=500)),
                ('category', models.CharField(default='General / Community', max_length=100)),
                ('in_initial_target_list', models.BooleanField(default=False)),
                ('keep_updated', models.BooleanField(default=True)),
                ('added_to_system_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField()),
                ('is_text_only', models.BooleanField()),
                ('is_original_content', models.BooleanField(default=False)),
                ('num_comments', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=1)),
                ('upvote_ratio', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('first_synced', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='subreddits.User')),
                ('subreddit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='subreddits.Subreddit')),
            ],
        ),
    ]
