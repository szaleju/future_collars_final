# Generated by Django 3.1.6 on 2021-02-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('publication_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
