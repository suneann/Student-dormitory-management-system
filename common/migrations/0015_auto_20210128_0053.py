# Generated by Django 3.1.5 on 2021-01-27 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_auto_20210128_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outer_info',
            name='Aapart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.apart_info'),
        ),
        migrations.AlterField(
            model_name='outer_info',
            name='Ocellphone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='outer_info',
            name='Oname',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='outer_info',
            name='Oouttime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='outer_info',
            name='Ops',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='outer_info',
            name='Osex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='Aroom',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='common.room_info'),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='Dmaj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.dmaj_info'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student_info',
            name='Sid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='Sname',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='Ssex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
    ]