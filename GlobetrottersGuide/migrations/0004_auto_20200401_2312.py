# Generated by Django 2.2.3 on 2020-04-01 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GlobetrottersGuide', '0003_auto_20200401_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='cityReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(verbose_name='date published')),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('timeSpent', models.DurationField()),
                ('image', models.ImageField(blank=True, upload_to='review_images')),
                ('text', models.TextField(max_length=2000)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('belong_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GlobetrottersGuide.City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='countryReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(verbose_name='date published')),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('timeSpent', models.DurationField()),
                ('image', models.ImageField(blank=True, upload_to='review_images')),
                ('text', models.TextField(max_length=2000)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('belong_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GlobetrottersGuide.Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='liked_review',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='liked_review_city',
            field=models.ManyToManyField(to='GlobetrottersGuide.cityReview'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='liked_review_country',
            field=models.ManyToManyField(to='GlobetrottersGuide.countryReview'),
        ),
    ]
