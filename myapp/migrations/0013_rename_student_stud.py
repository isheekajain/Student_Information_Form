# Generated by Django 3.2.9 on 2021-12-10 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_rename_students_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Stud',
        ),
    ]
