# Generated by Django 3.1.5 on 2021-01-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_auto_20210128_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='Sclass',
            field=models.IntegerField(),
        ),
    ]
