# Generated by Django 5.0 on 2024-06-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0003_testimonial_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='linkdin',
            field=models.URLField(blank=True, null=True),
        ),
    ]
