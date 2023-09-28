# Generated by Django 4.1.2 on 2023-09-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('rating', models.IntegerField()),
                ('about', models.TextField()),
                ('genere', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[('malayalam', 'Malayalam'), ('english', 'English'), ('hindi', 'Hindi'), ('tamil', 'Tamil')], max_length=10)),
                ('release_data', models.DateTimeField()),
                ('duration', models.FloatField()),
            ],
        ),
    ]
