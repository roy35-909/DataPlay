# Generated by Django 5.0 on 2024-05-15 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='course/content')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_order', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('learn', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='course/thumbnail')),
                ('course_price', models.DecimalField(decimal_places=2, default=2, max_digits=10, null=True)),
                ('content_price', models.DecimalField(decimal_places=2, default=2, max_digits=10, null=True)),
                ('course_price_discounted', models.DecimalField(decimal_places=2, default=2, max_digits=10, null=True)),
                ('content_price_discounted', models.DecimalField(decimal_places=2, default=2, max_digits=10, null=True)),
                ('course_duration', models.IntegerField(default=10)),
                ('course_percentage', models.IntegerField(default=10)),
                ('instructors', models.ManyToManyField(to='user.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='CourseContents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_free', models.BooleanField(default=False)),
                ('content_order', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('next_content', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev_content_relation', to='course.coursecontents')),
                ('prev_content', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_content_relation', to='course.coursecontents')),
                ('files', models.ManyToManyField(to='course.filefield')),
            ],
        ),
    ]
