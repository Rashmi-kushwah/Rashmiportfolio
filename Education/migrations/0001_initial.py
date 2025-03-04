# Generated by Django 4.2.19 on 2025-02-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_title', models.CharField(blank=True, max_length=200, null=True)),
                ('education_h1', models.CharField(blank=True, max_length=255, null=True)),
                ('education_name', models.CharField(blank=True, max_length=255, null=True)),
                ('institution_name', models.CharField(blank=True, max_length=255, null=True)),
                ('skill_name', models.CharField(blank=True, max_length=255, null=True)),
                ('skill_image', models.ImageField(blank=True, null=True, upload_to='Portfolio_image/')),
            ],
        ),
    ]
