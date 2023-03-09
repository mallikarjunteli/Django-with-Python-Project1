from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=50)

    def __str__(self):
        return f'(self.course_name)'

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
