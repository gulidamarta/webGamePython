# Generated by Django 2.2.4 on 2019-08-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0005_auto_20190812_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
