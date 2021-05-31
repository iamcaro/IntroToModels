from django.db import models


# Create your models here.

class School (models.Model):
    name = models.CharField(max_length=400)


class CertificateType (models.Model):
    name = models.CharField(max_length=400)

class Grade (models.Model):
    type = models.CharField(max_length=50)


class Faculty (models.Model):
    name = models.CharField(max_length=400)


class Department (models.Model):
    name = models.CharField(max_length=400)
    faculty = models.ForeignKey(Faculty, on_delete=models.CommaSeparatedIntegerField)


class Student (models.Model):
    full_name = models.CharField(max_length= 100)
    grad_year = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    