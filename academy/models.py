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
    title = models.CharField(max_length=50)
    material_url = models.URLField(blank=True, null=True)
    material_file = models.FileField(blank=True, null=True)
    activity = models.ManyToManyField(Activity)

    def __str__(self):
        return f'{self.title}'


class StudentsGroup (models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class AssignmentActivity(models.Model):    
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name='activity_assignments'
    )
    group = models.ForeignKey(
        StudentsGroup,
        on_delete=models.CASCADE,
        related_name='group_assignments'
    )

    def __str__(self):
        return f'{self.pk} - {self.activity.title} - Value: {self.activity.value} - Group: {self.group}'

    class Meta:
        verbose_name = 'Assignment activity'
        verbose_name_plural = 'Assignemnts activities'


class AssignmentDelivery (models.Model):
    score = models.IntegerField(blank=True, null=True)
    delivered = models.DateTimeField()
    anotation = models.CharField(max_length=250, blank=True, null=True)
    delivery_file = models.FileField(upload_to='delivery_files/', blank=True, null=True)
    delivery_url = models.URLField(blank=True, null=True)
    delivered = models.DateTimeField(auto_now=True, blank=True, null=True)
    student = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='student_deliveries'
    )
    assignment_activity = models.ForeignKey(
        AssignmentActivity,
        on_delete=models.CASCADE,
        related_name='assignment_deliveries'
    )

    def __str__(self):
        return f'{self.student.username} - {self.assignment_activity.activity.title} - Group: {self.assignment_activity.group}'

    class Meta:
        verbose_name = 'Assignment delivery'
        verbose_name_plural = 'Assignment deliveries'
