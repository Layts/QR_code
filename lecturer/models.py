from django.db import models


class Student(models.Model):
    """БД содержащая всех студентов,
    для вывода списком по QR коду"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    """Для записи новых лекций лекторами
    по кол-ву пришедших студентов"""
    name = models.CharField(max_length=200, default='default lecture')
    students_count = models.IntegerField()
    student = models.ManyToManyField(Student, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " № " + str(self.pk)

