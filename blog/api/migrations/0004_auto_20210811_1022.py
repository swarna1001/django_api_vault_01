# Generated by Django 3.1.7 on 2021-08-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210811_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
