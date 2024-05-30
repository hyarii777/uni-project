from django.db import models

class TableType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TableInfo(models.Model):
    table_type = models.ForeignKey(TableType, on_delete=models.CASCADE, related_name='tables')
    question = models.CharField(max_length=255)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.question

from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    student_number = models.CharField(max_length=20, unique=True, default='')
    name = models.CharField(max_length=100, default='')
    specialization = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    which_year = models.IntegerField(default=1)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(default='')

    tables = models.ManyToManyField('TableInfo', related_name='students', blank=True)

    def __str__(self):
        return self.name

    def get_questions_with_status(self):
        return ", ".join(
            [f"{table.table_type}: {table.question} (Is True: {table.is_true})" for table in self.tables.all()]
        )