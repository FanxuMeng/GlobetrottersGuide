# Generated by Django 2.2.3 on 2020-04-08 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GlobetrottersGuide', '0008_auto_20200404_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
