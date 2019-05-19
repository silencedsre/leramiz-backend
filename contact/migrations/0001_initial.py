# Generated by Django 2.2.1 on 2019-05-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
