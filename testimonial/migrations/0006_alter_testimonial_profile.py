# Generated by Django 5.0 on 2024-08-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0005_alter_testimonial_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='profile',
            field=models.FileField(null=True, upload_to='testimonial_profiles'),
        ),
    ]