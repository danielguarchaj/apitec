# Generated by Django 2.1 on 2019-05-28 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0017_auto_20190528_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentdelivery',
            name='reviewed',
        ),
    ]
