# Generated by Django 2.2.4 on 2019-08-12 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0006_auto_20190812_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='game',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game'),
        ),
    ]
