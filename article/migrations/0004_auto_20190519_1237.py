# Generated by Django 2.1.7 on 2019-05-19 04:37

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190517_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='author',
            field=models.ForeignKey(on_delete='on_delete=CASCADE', related_name='article', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='column',
            field=models.ForeignKey(on_delete='on_delete=CASADE', related_name='article_column', to='article.ArticleColumn'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 4, 37, 42, 591078, tzinfo=utc)),
        ),
    ]
