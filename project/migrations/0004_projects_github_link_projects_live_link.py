# Generated by Django 4.2.19 on 2025-02-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_remove_projects_project_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='github_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='live_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
