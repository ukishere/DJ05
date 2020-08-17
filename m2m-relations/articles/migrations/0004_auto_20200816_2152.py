# Generated by Django 2.2.10 on 2020-08-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200816_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag',
            field=models.TextField(choices=[('Здоровье', 'Здоровье'), ('Наука', 'Наука'), ('Город', 'Город')]),
        ),
    ]
