# Generated by Django 2.1.7 on 2019-05-20 06:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20190520_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 6, 29, 34, 167298, tzinfo=utc)),
        ),
    ]
