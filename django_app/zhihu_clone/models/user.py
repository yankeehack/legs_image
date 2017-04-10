from django.db import models
from imagekit.models import ProcessedImageField
from datetime import datetime
from imagekit.processors import ResizeToFill
from .question import Question
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        'Creates a User with the given username, email and password'
        email = UserManager.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200, null=True, blank=True)
    avatar = ProcessedImageField(upload_to='posts',
                                 processors=[ResizeToFill(100,50)],
                                 format='JPEG',
                                 options={'quality': 100})
    create_at = models.DateTimeField(default=datetime.now(), editable=False)
    update_at = models.DateTimeField(default=datetime.now())
    # *** ForeignField***
    # my_questions
    # my_comments
    # my_focus
    # my_answers
    # my_ups

    user_manager = UserManager()
    USERNAME_FIELD = 'email'

