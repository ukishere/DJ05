from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    students = models.ManyToManyField(
        'Student',
        related_name='students'
    )

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    group = models.CharField(max_length=10, verbose_name='Класс')

    teachers = models.ManyToManyField(
        Teacher,
        through='Students_to_Teachers',
        related_name='teachers')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name

class Students_to_Teachers(models.Model):

    students = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    teachers = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (('teachers','students'),)
        db_table = 'Students_to_Teachers'