# Generated by Django 3.1.6 on 2021-03-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_auto_20210318_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/dafault.jpg/', upload_to='profile_pics'),
        ),
    ]