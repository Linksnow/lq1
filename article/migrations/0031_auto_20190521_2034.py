# Generated by Django 2.1.7 on 2019-05-21 12:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0030_auto_20190521_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 12, 34, 12, 992239, tzinfo=utc)),
        ),
    ]
