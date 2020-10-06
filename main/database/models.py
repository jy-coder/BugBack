from django.db import models

# Create your models here.

class Role (models.Model):
    REPORTER = 'REPORTER'
    DEVELOPER = 'DEVELOPER'
    REVIEWER = 'REVIEWER'
    TRIAGER = 'TRIAGER'

    ROLE_CHOICES =  [
        ('REPORTER', 'Reporter'),
        ('DEVELOPER', 'Developer'),
        ('REVIEWER', 'Reviewer'),
        ('TRIAGER', 'Triager'),
    ]

    role_title = models.CharField(max_length=50,
        choices=ROLE_CHOICES,null=True)

    class Meta:
        db_table = "roles"

class User (models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = "users"

class Bug (models.Model):
    name = models.CharField(null=True,max_length=1000)
    status = models.CharField(null=True,max_length=1000)
    developer_assigned = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        db_table = "bugs"




