# Generated by Django 3.2.9 on 2021-12-07 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20211207_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stud',
            name='images',
        ),
    ]
