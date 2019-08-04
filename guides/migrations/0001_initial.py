# Generated by Django 2.2.4 on 2019-08-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('course_name', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('price', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]