# Generated by Django 2.2.3 on 2020-04-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GlobetrottersGuide', '0005_auto_20200402_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='liked_review_city',
            field=models.ManyToManyField(blank=True, to='GlobetrottersGuide.cityReview'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='liked_review_country',
            field=models.ManyToManyField(blank=True, to='GlobetrottersGuide.countryReview'),
        ),
    ]
