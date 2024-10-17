from django.db import models
from user.models import User


class Task(models.Model):

    date_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.DO_NOTHING, verbose_name='Usuário', related_name='task_user')
    description = models.TextField(max_length=2500, verbose_name='Descrição', help_text='Escreva a descrição da sua tarefa')

    class Meta:
        ordering = ['-date_create']
