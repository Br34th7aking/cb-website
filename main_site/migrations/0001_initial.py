# Generated by Django 2.2.4 on 2019-08-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('link', models.URLField(max_length=300)),
                ('contributor', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
