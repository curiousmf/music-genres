# Generated by Django 4.2.1 on 2023-06-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pop', '0002_pop_singer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pop_singer',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
