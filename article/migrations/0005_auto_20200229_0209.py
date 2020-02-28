# Generated by Django 2.1.4 on 2020-02-28 18:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0004_auto_20200229_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepost',
            name='users_like',
        ),
        migrations.AddField(
            model_name='articlepost',
            name='user_like',
            field=models.ManyToManyField(blank=True, related_name='articles_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
