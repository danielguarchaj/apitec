# Generated by Django 2.1 on 2019-05-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0011_remove_studentsgroup_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentdelivery',
            name='delivered',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
