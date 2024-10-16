# Generated by Django 5.1.2 on 2024-10-17 19:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(help_text='Escreva a descrição da sua tarefa', max_length=2500, verbose_name='Descrição')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='task_user', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'ordering': ['-date_create'],
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(help_text='Escreva a descrição da sua atividade', max_length=2500, verbose_name='Descrição')),
                ('minutes', models.PositiveIntegerField(help_text='Duração total em minutos', verbose_name='Duração')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='register_task', to='task.task')),
            ],
        ),
    ]
