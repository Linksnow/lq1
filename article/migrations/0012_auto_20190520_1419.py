# Generated by Django 2.1.7 on 2019-05-20 06:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20190520_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 6, 19, 3, 616682, tzinfo=utc)),
        ),
    ]