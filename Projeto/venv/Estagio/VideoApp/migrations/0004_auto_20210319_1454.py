# Generated by Django 3.1.7 on 2021-03-19 17:54

import VideoApp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VideoApp', '0003_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='videos',
            field=models.FileField(default='default.mp4', upload_to='video/%y', validators=[VideoApp.validators.file_size]),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
