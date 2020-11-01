from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save



class Profile(models.Model):
    ROLE_CHOICES = [
        ('user','user'), 
        ('developer','developer'),
        ('triager','triager'),
        ('reviewer','reviewer'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    role_title = models.CharField(max_length=50,null=True,choices=ROLE_CHOICES)
    expertise = models.IntegerField(default=0)

    class Meta:
        db_table = "profile"





class Bug (models.Model):
    class Meta:
        db_table = "bugs"
    name = models.CharField(null=True,max_length=1000)
    description = models.CharField(null=True,max_length=1000)
    status = models.CharField(null=True,max_length=1000,default="active")
    priority = models.CharField(null=True,max_length=1000)
    reported_by = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='user')
    developer_assigned = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='developer')
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BugUserLikes(models.Model):
    class Meta:
        db_table = "bug_user_like"
    user_id = models.IntegerField(null=True)
    bug_id = models.IntegerField(null=True)

class CommentUserLikes(models.Model):
    class Meta:
        db_table = "comment_user_like"
    comment_id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)


class Comment (models.Model):
    comment_text = models.CharField(null=True,max_length=1000)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bug_id = models.IntegerField(null=True)
    class Meta:
        db_table = "comments"






