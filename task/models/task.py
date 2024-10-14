from django.db import models
from user.models import User


class Task(models.Model):

    date_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='task_user')
    time = models.TimeField(verbose_name='Time to conclude')
    description = models.TextField(max_length=2500, verbose_name='Description')