# Generated by Django 3.1.2 on 2020-10-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_video_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pics/thumbnails'),
        ),
    ]
