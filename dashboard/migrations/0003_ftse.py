# Generated by Django 3.0.4 on 2020-04-27 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_auto_20200427_1803"),
    ]

    operations = [
        migrations.CreateModel(
            name="FTSE",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("date", models.DateField(default=datetime.date.today, verbose_name="Date")),
                ("open", models.FloatField()),
                ("close", models.FloatField()),
                ("low", models.FloatField()),
                ("high", models.FloatField()),
                ("volume", models.CharField(max_length=100)),
            ],
            options={"ordering": ("date",),},
        ),
    ]