# Generated by Django 2.2.1 on 2019-05-14 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_number', models.PositiveIntegerField(null=True)),
                ('street_address', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('area', models.PositiveIntegerField(null=True)),
                ('bedrooms', models.PositiveIntegerField(null=True)),
                ('agent_name', models.CharField(max_length=200)),
                ('garages', models.PositiveIntegerField(null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2019, 5, 14, 18, 1, 16, 117980))),
                ('price', models.PositiveIntegerField(null=True)),
                ('featured', models.BooleanField(default=False)),
                ('rent_or_sale', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
