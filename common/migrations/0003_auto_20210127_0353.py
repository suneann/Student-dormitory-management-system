# Generated by Django 3.1.5 on 2021-01-26 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20210127_0335'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='room_info',
            unique_together={('Rroom', 'RFAinfo')},
        ),
    ]
