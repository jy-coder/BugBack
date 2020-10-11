from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Role (models.Model):
    ROLE_CHOICES = [
        ('user','user'), 
        ('developer','developer'),
        ('triager','triager'),
        ('reviewer','reviewer'),
    ]

    role_title = models.CharField(max_length=50,null=True,choices=ROLE_CHOICES)



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    username = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=100,null=False)
    role = models.ForeignKey(Role, null=True, default=None, on_delete=models.SET_NULL)


    USERNAME_FIELD = 'username'

 
    class Meta:
        db_table = "users"


class Comment (models.Model):
    comment_text = models.CharField(null=True,max_length=1000)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)
    class Meta:
        db_table = "comments"


class Bug (models.Model):


    def validate_developer_assigned(self):
        developer = self.cleaned_data.get("developer_assigned")
        print(developer)



    class Meta:
        db_table = "bugs"


    name = models.CharField(null=True,max_length=1000)
    status = models.CharField(null=True,max_length=1000)
    priority = models.CharField(null=True,max_length=1000)
    developer_assigned = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    comment = models.ForeignKey(Comment, null=True, default=None, on_delete=models.SET_NULL)
    upvote_count =  models.IntegerField(default=0)
    downvote_count =  models.IntegerField(default=0)







