# Generated by Django 5.0 on 2024-09-11 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_filefield_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecontents',
            name='delete_status',
            field=models.BooleanField(default=False),
        ),
    ]