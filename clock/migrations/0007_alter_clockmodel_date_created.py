# Generated by Django 4.1 on 2022-12-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock', '0006_alter_clockmodel_clock_alter_clockmodel_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clockmodel',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
