# Generated by Django 5.0 on 2024-05-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='coursecontents',
            name='video_link',
            field=models.ManyToManyField(to='course.videolinks'),
        ),
    ]
