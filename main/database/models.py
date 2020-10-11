from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save


#######for testing endpoint -can remove later########
class Role (models.Model):
    ROLE_CHOICES = [
        ('user','user'), 
        ('developer','developer'),
        ('triager','triager'),
        ('reviewer','reviewer'),
    ]

    role_title = models.CharField(max_length=50,null=True,choices=ROLE_CHOICES)



class Profile(models.Model):
    ROLE_CHOICES = [
        ('user','user'), 
        ('developer','developer'),
        ('triager','triager'),
        ('reviewer','reviewer'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    role_title = models.CharField(max_length=50,null=True,choices=ROLE_CHOICES)

    class Meta:
        db_table = "profile"

    ## anything added into the user database will be added here
    # change role_title here when populating database

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance,role_title='user')


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Comment (models.Model):
    comment_text = models.CharField(null=True,max_length=1000)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
    reported_by = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='user')
    developer_assigned = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='developer')
    comment = models.ForeignKey(Comment, null=True, default=None, on_delete=models.SET_NULL)
    upvote_count =  models.IntegerField(default=0)
    downvote_count =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    ######## can validate developer is developer, reported by is user ###################







