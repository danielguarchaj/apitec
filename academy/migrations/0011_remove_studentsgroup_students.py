# Generated by Django 2.1 on 2019-05-27 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0010_auto_20190527_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsgroup',
            name='students',
        ),
    ]
