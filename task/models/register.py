from django.db import models
from task.models import Task


class Register(models.Model):

    date_create = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, models.DO_NOTHING, related_name='register_task')
    description = models.TextField(max_length=2500, verbose_name='Descrição', help_text='Escreva a descrição da sua atividade')
    minutes = models.PositiveIntegerField(verbose_name='Duração', help_text='Duração total em minutos')

    def cast_time(self):
        days = self.minutes // (24 * 60)
        hours = (self.minutes % (24 * 60)) // 60
        minutes = self.minutes % 60

        result = []

        if days > 0:
            result.append(f"{days} dia{'s' if days > 1 else ''}")
        if hours > 0:
            result.append(f"{hours} hora{'s' if hours > 1 else ''}")

        if minutes > 0 or self.minutes == 0:
            result.append(f"{minutes} minuto{'s' if minutes > 1 else ''}")

        return ', '.join(result)
