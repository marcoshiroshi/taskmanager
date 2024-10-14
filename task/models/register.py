from django.db import models
from task.models import Task

class Register(models.Model):

    date_create = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, models.DO_NOTHING, related_name='register_task')
    description = models.TextField(max_length=2500, verbose_name='Description')