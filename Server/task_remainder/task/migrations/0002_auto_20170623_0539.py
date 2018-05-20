# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-23 05:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.TimeField(blank=True, help_text=b'Time format is :HH:MM:SS', null=True)),
                ('message', models.TextField(max_length=500)),
            ],
            options={
                'db_table': 'notification',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'person_record',
            },
        ),
        migrations.RemoveField(
            model_name='task',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='modified_time',
        ),
        migrations.AddField(
            model_name='task',
            name='reminder_time',
            field=models.TimeField(blank=True, help_text=b'Time format is :HH:MM:SS', null=True),
        ),
        migrations.AlterModelTable(
            name='task',
            table='task',
        ),
        migrations.AddField(
            model_name='notification',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notify_user', to='task.Person'),
        ),
        migrations.AddField(
            model_name='task',
            name='person_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='task_user', to='task.Person'),
            preserve_default=False,
        ),
    ]
