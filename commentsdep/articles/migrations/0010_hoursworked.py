# Generated by Django 3.1.6 on 2021-03-12 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0009_article_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoursWorked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('hour_count', models.DecimalField(decimal_places=2, max_digits=2)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
