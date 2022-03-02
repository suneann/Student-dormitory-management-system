# Generated by Django 3.1.5 on 2021-01-26 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20210127_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor_info',
            name='Lfloor',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='room_info',
            name='Rroom',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='Aroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.room_info'),
        ),
    ]