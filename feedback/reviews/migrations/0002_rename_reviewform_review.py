# Generated by Django 4.2.3 on 2023-08-26 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReviewForm',
            new_name='Review',
        ),
    ]
