# Generated by Django 3.2.6 on 2021-08-09 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210809_1618'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Togaraklar',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Pulli_Kurslar',
            new_name='PaidCourse',
        ),
    ]