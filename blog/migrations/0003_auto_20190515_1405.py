# Generated by Django 2.2.1 on 2019-05-15 08:20

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_blog_headline'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blog',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
