# Generated by Django 3.1.6 on 2021-03-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20210314_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoursworked',
            name='hour_count',
            field=models.DurationField(null=True),
        ),
    ]
