# Generated by Django 2.1 on 2019-05-30 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0019_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignmentactivity',
            options={'verbose_name': 'Activity Assignment', 'verbose_name_plural': 'Activity Assignments'},
        ),
        migrations.AlterModelOptions(
            name='assignmentdelivery',
            options={'verbose_name': 'Student delivery', 'verbose_name_plural': 'Student deliveries'},
        ),
    ]
