from django.db import models
from .base_model import Base
from .user import User


class Question(Base):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey('User', related_name='my_questions')
    comment_ids = models.ManyToManyField('User', related_name='my_comments')
    deleted = models.BooleanField()
    focus_ids = models.ManyToManyField('User', related_name='my_focus')
    view_count = models.BigIntegerField()

    # tags in topic model


    class Meta(Base.Meta):
        pass