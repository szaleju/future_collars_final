# Generated by Django 3.1.6 on 2021-03-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0027_profile_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='snippet',
            field=models.CharField(max_length=120, verbose_name='Snippet'),
        ),
    ]
