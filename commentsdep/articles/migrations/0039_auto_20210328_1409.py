# Generated by Django 3.1.6 on 2021-03-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0038_auto_20210328_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslip',
            name='month',
            field=models.IntegerField(),
        ),
    ]
