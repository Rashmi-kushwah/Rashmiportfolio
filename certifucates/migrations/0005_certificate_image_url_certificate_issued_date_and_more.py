# Generated by Django 4.2.19 on 2025-02-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifucates', '0004_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='issued_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='organization',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
