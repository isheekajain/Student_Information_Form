# Generated by Django 3.2.9 on 2021-12-10 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_stud_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='docs',
        ),
    ]
