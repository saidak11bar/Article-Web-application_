# Generated by Django 5.1 on 2024-08-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('author_full_name', models.CharField(max_length=100)),
                ('author_image', models.ImageField(upload_to='images_author/')),
                ('author_job', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
