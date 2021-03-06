# Generated by Django 3.2.13 on 2022-04-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='language',
            field=models.ManyToManyField(to='movies.Language'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
    ]
