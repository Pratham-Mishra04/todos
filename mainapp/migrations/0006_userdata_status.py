# Generated by Django 4.0.2 on 2022-02-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_userdata_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]