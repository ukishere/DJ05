# Generated by Django 2.2.10 on 2020-08-17 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20200817_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='students',
        ),
    ]
