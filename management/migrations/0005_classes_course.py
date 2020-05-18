# Generated by Django 2.2.7 on 2020-04-17 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20200417_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hindi', models.CharField(max_length=50)),
                ('English', models.CharField(max_length=50)),
                ('Maths', models.CharField(max_length=50)),
                ('Science', models.CharField(max_length=50)),
                ('SocialScience', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.faculty_model')),
            ],
        ),
    ]