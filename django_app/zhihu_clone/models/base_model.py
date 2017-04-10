from datetime import datetime
from django.db import models


class Base(models.Model):
    create_at = models.DateTimeField(default=datetime.now(), editable=False)
    update_at = models.DateTimeField(default=datetime.now())
    is_edit = models.BooleanField(default=False)

    class Meta:
        # make sure no table will be created for this class
        abstract = True
        ordering = ["update_on"]