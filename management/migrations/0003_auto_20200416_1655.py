# Generated by Django 2.2.7 on 2020-04-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20200416_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_model',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]