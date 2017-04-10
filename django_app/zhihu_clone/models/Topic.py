from base_model import Base
from django.db import models
from .question import Question


class Topic(Base):
    # null = true mean in db, this field could be null
    # blank = true mean in form, could accept this field without value
    tag = models.CharField(max_length=200, null=True, blank=True)
    # this will add field question_tags in question model
    question_id = models.ManyToManyField('Question', blank=True, null=True, related_name='tags')
    question_title = models.CharField(max_length=200, null=True, blank=True)

    class Meta(Base.Meta):
        # when override meta class, default abstract will be false, placeholder here
        pass
