# Generated by Django 4.1.2 on 2023-09-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='image',
            field=models.ImageField(upload_to='movie_cast_images/'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='movie_images/'),
        ),
    ]
