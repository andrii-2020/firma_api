# Generated by Django 4.1 on 2022-12-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clockmodel',
            name='date_created',
            field=models.DateField(blank=True),
        ),
    ]
