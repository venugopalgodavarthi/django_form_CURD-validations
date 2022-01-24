# Generated by Django 3.2.4 on 2022-01-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customermodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[['Male', 'MALE'], ['Female', 'FEMALE']], max_length=15)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]