# Generated by Django 2.2.10 on 2020-08-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200817_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_to_teacher',
            old_name='student',
            new_name='students',
        ),
        migrations.RenameField(
            model_name='student_to_teacher',
            old_name='teacher',
            new_name='teachers',
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(related_name='students', to='school.Student'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(through='school.Student_to_Teacher', to='school.Teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='student_to_teacher',
            unique_together={('teachers', 'students')},
        ),
    ]