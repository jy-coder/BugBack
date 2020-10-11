from django.db import models
from django.contrib.auth.models import User


class Role (models.Model):
    ROLE_CHOICES = [
        ('user','user'), 
        ('developer','developer'),
        ('triager','triager'),
        ('reviewer','reviewer'),
    ]
        
    role_title = models.CharField(max_length=50,null=True,choices=ROLE_CHOICES)

    class Meta:
        db_table = "roles"





class Comment (models.Model):
    comment_text = models.CharField(null=True,max_length=1000)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        db_table = "comments"


class Employee(models.Model):
   user = models.OneToOneField(User,null=True, on_delete=models.SET_NULL)
   role = models.OneToOneField(Role,null=True, on_delete=models.SET_NULL)


class Bug (models.Model):
    name = models.CharField(null=True,max_length=1000)
    status = models.CharField(null=True,max_length=1000)
    priority = models.CharField(null=True,max_length=1000)
    developer_assigned = models.ForeignKey(Employee,null=True,on_delete=models.SET_NULL)
    comment = models.ForeignKey(Comment, null=True, default=None, on_delete=models.SET_NULL)
    upvote_count =  models.IntegerField(default=0)
    downvote_count =  models.IntegerField(default=0)

    def validate_developer_assigned(self):
        developer = self.cleaned_data.get("developer_assigned")
        print(developer)

    class Meta:
        db_table = "bugs"







