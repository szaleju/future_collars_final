# Generated by Django 3.1.6 on 2021-03-17 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20210317_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoursworked',
            name='hour_count',
        ),
        migrations.RemoveField(
            model_name='hoursworked',
            name='logged',
        ),
    ]
