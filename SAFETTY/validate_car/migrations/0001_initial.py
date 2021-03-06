# Generated by Django 3.1.5 on 2021-02-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_model_year', models.CharField(max_length=128)),
                ('license_plate', models.CharField(max_length=128)),
                ('colour', models.CharField(max_length=128)),
                ('route', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('dob', models.IntegerField()),
                ('permit_number', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=256)),
                ('contact_number', models.CharField(max_length=128)),
            ],
        ),
    ]
