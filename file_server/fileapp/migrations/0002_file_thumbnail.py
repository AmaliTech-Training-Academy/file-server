# Generated by Django 4.1.6 on 2023-02-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/thumbnails/'),
        ),
    ]
