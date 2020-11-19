from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    ROLE_CHOICES = [
        ('reporter','reporter'), 
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BugUserLikes(models.Model):
    class Meta:
        db_table = "bug_user_like"
    user_id = models.IntegerField(null=True)
    bug_id = models.IntegerField(null=True)



class Comment (models.Model):
    comment_text = models.CharField(null=True,max_length=1000)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bug_id = models.IntegerField(null=True)
    class Meta:
        db_table = "comments"


##THIS IS USER MODEL COMBINE WITH PROFILE MODEL
# User model is from django.contrib.auth.models.User 
# user model is making use of this class
# class AbstractUser(AbstractBaseUser, PermissionsMixin):
#     """
#     An abstract base class implementing a fully featured User model with
#     admin-compliant permissions.

#     Username and password are required. Other fields are optional.
#     """
#     username_validator = UnicodeUsernameValidator()

#     username = models.CharField(
#         _('username'),
#         max_length=150,
#         unique=True,
#         help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
#         validators=[username_validator],
#         error_messages={
#             'unique': _("A user with that username already exists."),
#         },
#     )
#     first_name = models.CharField(_('first name'), max_length=150, blank=True)
#     last_name = models.CharField(_('last name'), max_length=150, blank=True)
#     email = models.EmailField(_('email address'), blank=True)
#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_('Designates whether the user can log into this admin site.'),
#     )
#     is_active = models.BooleanField(
#         _('active'),
#         default=True,
#         help_text=_(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),
#     )
#     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

#     objects = UserManager()

#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#         abstract = True

#     def clean(self):
#         super().clean()
#         self.email = self.__class__.objects.normalize_email(self.email)

#     def get_full_name(self):
#         """
#         Return the first_name plus the last_name, with a space in between.
#         """
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         """Return the short name for the user."""
#         return self.first_name

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         """Send an email to this user."""
#         send_mail(subject, message, from_email, [self.email], **kwargs)



class Reporter(models.Model):
    reporter_id = models.IntegerField(null=True)


class Developer(models.Model):
    developer_id = models.IntegerField(null=True)


class Reviewer(models.Model):
    reviewer_id = models.IntegerField(null=True)


class Triager(models.Model):
    triager_id = models.IntegerField(null=True)
