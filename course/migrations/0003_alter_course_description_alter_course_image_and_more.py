# Generated by Django 5.0 on 2024-05-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_videolinks_coursecontents_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course/thumbnail'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coursecontents',
            name='files',
            field=models.ManyToManyField(null=True, to='course.filefield'),
        ),
        migrations.AlterField(
            model_name='coursecontents',
            name='video_link',
            field=models.ManyToManyField(null=True, to='course.videolinks'),
        ),
    ]