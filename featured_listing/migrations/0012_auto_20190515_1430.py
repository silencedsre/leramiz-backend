# Generated by Django 2.2.1 on 2019-05-15 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featured_listing', '0011_auto_20190515_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredlisting',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 15, 14, 30, 45, 64787)),
        ),
    ]
