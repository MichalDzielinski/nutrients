# Generated by Django 4.2.4 on 2023-09-02 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Calories',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
