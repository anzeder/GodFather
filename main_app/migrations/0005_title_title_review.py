# Generated by Django 3.1.7 on 2021-04-21 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210421_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='title_review',
            field=models.TextField(default='Some random review'),
        ),
    ]
