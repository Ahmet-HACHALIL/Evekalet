# Generated by Django 3.1.4 on 2021-05-07 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0008_auto_20210507_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]