# Generated by Django 2.2.1 on 2019-05-19 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featured_listing', '0017_auto_20190519_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredlisting',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 15, 55, 28, 762027)),
        ),
    ]