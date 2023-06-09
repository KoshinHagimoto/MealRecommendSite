# Generated by Django 4.1.7 on 2023-04-05 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Meal')),
                ('imageUrl', models.CharField(max_length=200, verbose_name='URL')),
                ('countryOfOrigin', models.CharField(max_length=120, verbose_name='Country')),
                ('description', models.TextField(verbose_name='Description')),
                ('dataAdded', models.DateTimeField(auto_now_add=True, verbose_name='create')),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tag')),
            ],
        ),
        migrations.CreateModel(
            name='MealRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('dateOfRating', models.DateTimeField(auto_now_add=True, verbose_name='Create')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MealSite.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MealRating',
                'verbose_name_plural': 'MealRatings',
            },
        ),
        migrations.AddField(
            model_name='meal',
            name='tag',
            field=models.ManyToManyField(to='MealSite.tag', verbose_name='Tag'),
        ),
    ]
