# Generated by Django 4.1.7 on 2023-04-05 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MealSite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='dataAdded',
            new_name='dateAdded',
        ),
    ]