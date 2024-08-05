# Generated by Django 5.0 on 2024-06-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_coursecontents_files_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecontents',
            name='files',
        ),
        migrations.RemoveField(
            model_name='coursecontents',
            name='video_link',
        ),
        migrations.AddField(
            model_name='coursecontents',
            name='files',
            field=models.ManyToManyField(blank=True, null=True, to='course.filefield'),
        ),
        migrations.AddField(
            model_name='coursecontents',
            name='video_link',
            field=models.ManyToManyField(blank=True, null=True, to='course.videolinks'),
        ),
    ]
