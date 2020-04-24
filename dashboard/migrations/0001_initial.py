# Generated by Django 3.0.4 on 2020-04-24 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('time', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('tweet', models.TextField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('replies_count', models.IntegerField()),
                ('retweets_count', models.IntegerField()),
                ('likes_count', models.IntegerField()),
                ('popular', models.BooleanField()),
                ('verified', models.BooleanField()),
                ('output', models.CharField(max_length=10)),
                ('positive', models.DecimalField(decimal_places=5, max_digits=10)),
                ('negative', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
