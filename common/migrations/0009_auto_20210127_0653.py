# Generated by Django 3.1.5 on 2021-01-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20210127_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pprice_info',
            name='Pid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
