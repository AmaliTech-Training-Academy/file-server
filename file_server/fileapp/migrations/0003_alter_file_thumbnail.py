# Generated by Django 4.1.6 on 2023-02-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapp', '0002_file_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
