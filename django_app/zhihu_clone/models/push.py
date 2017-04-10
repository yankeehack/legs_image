from django.db import models
from datetime import datetime
from .question import Question
from .user import User
from .answer import Answer


class Push(models.Model):
    push_type_choices = (
        (0, 'online'),
        (1, 'offline'),
        (2, 'sucker'),
    )

    push_type = models.IntegerField(choices=push_type_choices)
    create_at = models.DateTimeField(default=datetime.now())
    user_id = models.ForeignKey('User')
    question_id = models.ForeignKey('Question')
    answer_id = models.ForeignKey('Answer')