# Generated by Django 3.1.6 on 2021-03-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0028_auto_20210322_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=16, verbose_name='word')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publication_datetime']},
        ),
    ]
