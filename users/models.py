from django.db import models

from django.contrib.auth import get_user_model
from academy.models import StudentsGroup

class Student(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True
    )
    groups = models.ManyToManyField(StudentsGroup)
    avatar = models.ImageField(blank=True, null=True, upload_to='student_avatars/')
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    emergency_phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__ (self):
        return f'{self.user.username} - {self.user.first_name} {self.user.last_name}'
