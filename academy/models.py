from django.db import models
from django.contrib.auth import get_user_model


class Language(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title


class Activity(models.Model):
    title = models.CharField(max_length=100)
    instructions = models.CharField(max_length=500)
    value = models.IntegerField()
    difficulty_level = models.IntegerField()
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='language_activities'
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='module_activities'
    )

    def __str__(self):
        return f'{self.title} - Value: {self.value} - Level: {self.difficulty_level} - Language: {self.language} - Module: {self.module}'


class SupportMaterial(models.Model):
    MATERIAL_TYPES = (
        ('0', 'Link'),
        ('1', 'File'),
        ('2', 'Video'),
    )
    title = models.CharField(max_length=50)
    material_type = models.CharField(max_length=1, choices=MATERIAL_TYPES, default='0')
    material_url = models.URLField(blank=True, null=True)
    material_file = models.FileField(blank=True, null=True)
    activity = models.ManyToManyField(Activity)

    def __str__(self):
        return f'{self.title} - {self.material_type}'


class AssignmentActivity(models.Model):
    score = models.IntegerField(blank=True, null=True)
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    delivered = models.DateTimeField(blank=True, null=True)
    file_assignment = models.FileField(upload_to='assignment_files/', blank=True, null=True)
    url_assignment = models.URLField(blank=True, null=True)
    student = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='student_assignments'
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name='activity_assignments'
    )