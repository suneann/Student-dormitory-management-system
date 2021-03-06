# Generated by Django 3.1.5 on 2021-01-27 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20210127_0656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apart_info',
            options={'verbose_name_plural': '公寓信息'},
        ),
        migrations.AlterModelOptions(
            name='dmaj_info',
            options={'verbose_name_plural': '专业信息'},
        ),
        migrations.AlterModelOptions(
            name='floor_info',
            options={'verbose_name_plural': '楼层信息'},
        ),
        migrations.AlterModelOptions(
            name='outer_info',
            options={'verbose_name_plural': '外来人员信息'},
        ),
        migrations.AlterModelOptions(
            name='pprice_info',
            options={'verbose_name_plural': '财务信息'},
        ),
        migrations.AlterModelOptions(
            name='room_info',
            options={'verbose_name_plural': '寝室信息'},
        ),
        migrations.AlterModelOptions(
            name='student_info',
            options={'verbose_name_plural': '学生信息'},
        ),
        migrations.AddField(
            model_name='student_info',
            name='Sclass',
            field=models.IntegerField(default=101),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student_info',
            name='Aroom',
            field=models.ForeignKey(blank=True, default=7, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.room_info'),
        ),
        migrations.AlterUniqueTogether(
            name='floor_info',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='room_info',
            unique_together=set(),
        ),
    ]
