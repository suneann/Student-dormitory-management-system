# Generated by Django 3.1.5 on 2021-01-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20210127_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor_info',
            name='Lfloor',
            field=models.CharField(blank=True, default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room_info',
            name='Rroom',
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
    ]