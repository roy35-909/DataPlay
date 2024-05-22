# Generated by Django 5.0 on 2024-05-15 16:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('bio', models.TextField(blank=True, null=True)),
                ('Designation', models.TextField(blank=True, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_pic', models.ImageField(default='default_profile.jpg', upload_to='profiles/instractor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
