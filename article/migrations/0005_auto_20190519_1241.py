# Generated by Django 2.1.7 on 2019-05-19 04:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20190519_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 4, 41, 9, 729040, tzinfo=utc)),
        ),
    ]
