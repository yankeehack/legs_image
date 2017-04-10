from .base_model import Base
from django.db import models
from .question import Question
from .user import User


class Answer(Base):
    question_id = models.ForeignKey('Question', related_name='answers')
    author_id = models.ForeignKey('User', related_name='my_answers')
    content = models.TextField()
    ups_id = models.ManyToManyField('User', related_name='my_ups')
    ups_num = models.IntegerField()
    downs = models.IntegerField()
    deleted = models.BooleanField()
    
    class Meta(Base.Meta):
        pass