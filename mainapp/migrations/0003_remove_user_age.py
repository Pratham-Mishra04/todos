# Generated by Django 4.0.2 on 2022-02-18 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_userdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
