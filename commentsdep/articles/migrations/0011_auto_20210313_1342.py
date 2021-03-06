# Generated by Django 3.1.6 on 2021-03-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_hoursworked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoursworked',
            name='day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hoursworked',
            name='hour_count',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
    ]
