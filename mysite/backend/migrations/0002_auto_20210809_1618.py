# Generated by Django 3.2.6 on 2021-08-09 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaidCourse',
            new_name='Pulli_Kurslar',
        ),
        migrations.RenameModel(
            old_name='Course',
            new_name='Togaraklar',
        ),
    ]