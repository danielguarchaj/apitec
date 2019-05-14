# Generated by Django 2.1 on 2019-05-14 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitySupportMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.Activity')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.SupportMaterial')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='assignmentactivity',
            name='score',
        ),
        migrations.RemoveField(
            model_name='assignmentactivity',
            name='student',
        ),
        migrations.AddField(
            model_name='assignmentactivity',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignmentreview',
            name='assignment_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_activity_reviews', to='academy.AssignmentActivity'),
        ),
    ]
