# Generated by Django 2.1.4 on 2020-03-05 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('created',)},
        ),
    ]
