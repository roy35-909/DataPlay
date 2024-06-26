# Generated by Django 5.0 on 2024-06-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_coursecontents_files_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursecontents',
            options={'ordering': ['content_order']},
        ),
        migrations.RemoveField(
            model_name='coursecontents',
            name='next_content',
        ),
        migrations.RemoveField(
            model_name='coursecontents',
            name='prev_content',
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='course/thumbnail'),
        ),
    ]
