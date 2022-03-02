# -*- coding: UTF-8 -*-
from django.db import models
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver

# Create your models here.

##专业实体
class Dmaj_info(models.Model):
    # 专业
    Dmaj = models.CharField(max_length=35,db_column='mojor')
    # 学院
    Ddep = models.CharField(max_length=35,db_column='college')
    class Meta:
        verbose_name_plural = "专业信息"
    def __str__(self):
        return '{} {}专业'.format(self.Ddep, self.Dmaj)

##公寓楼实体
class Apart_info(models.Model):
    Aapart = models.CharField(max_length=20, primary_key=True,db_column='apartment')
    class Meta:
        verbose_name_plural = "公寓信息"
    def __str__(self):
        return '{}'.format(self.Aapart)


##楼层实体
class Floor_info(models.Model):
    Lfloor = models.CharField(max_length=35,db_column='floor')
    Lapart = models.ForeignKey(Apart_info, on_delete=models.CASCADE, null=True, related_name='Floor_apart',db_column='apartment')

    class Meta:
        unique_together = (('Lfloor', 'Lapart'),)
    class Meta:
        verbose_name_plural = "楼层信息"
    def __str__(self):
        return '{}{}'.format(self.Lapart, self.Lfloor)


##寝室实体
class Room_info(models.Model):
    Rroom = models.IntegerField(db_column='dormitory number')
    RFAinfo = models.ForeignKey(Floor_info, on_delete=models.CASCADE, related_name='Room_Floor_apart',db_column='apartment')
    Rlimit = models.IntegerField(db_column='upper limit')
    exists = models.IntegerField(db_column='current residents')

    class Meta:
        unique_together = (('Rroom', 'RFAinfo'),)
    class Meta:
        verbose_name_plural = "寝室信息"
    def __str__(self):
        return '{} {}:{}/{}'.format(self.RFAinfo, self.Rroom, self.exists, self.Rlimit)



##学生实体
class Student_info(models.Model):
    STUDENT_SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    # 学号
    Sid = models.IntegerField(primary_key=True)
    # 姓名
    Sname = models.CharField(max_length=35)
    # 性别
    Ssex = models.CharField(max_length=10, choices=STUDENT_SEX)
    #班级
    Sclass = models.IntegerField()
    # 专业
    Dmaj = models.ForeignKey('Dmaj_info', on_delete=models.CASCADE)
    # 寝室号
    Aroom = models.ForeignKey('Room_info', on_delete=models.CASCADE,default = 7)

    class Meta:
        verbose_name_plural = "学生信息"

    def __str__(self):
        return '{} {}'.format(self.Sid, self.Sname)


##外来人员实体
class Outer_info(models.Model):
    OURYER_SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    # 姓名
    Oname = models.CharField(max_length=35)
    # 性别
    Osex = models.CharField(max_length=10, choices=OURYER_SEX)
    # 联系方式
    Ocellphone = models.IntegerField()
    # 公寓楼
    Aapart = models.ForeignKey('Apart_info', on_delete=models.CASCADE, null=True)
    # 来访时间
    Ointime = models.DateField(db_column='visiting time')
    # 离开时间
    Oouttime = models.DateField(blank=True, null=True)
    # 备注
    Ops = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "外来人员信息"

    def __str__(self):
        return '{} {}'.format(self.Aapart, self.Oname)

##财务实体
class Pprice_info(models.Model):
    # 编号
    Pid = models.AutoField(primary_key=True)
    # 公寓楼
    Aapart = models.ForeignKey('Apart_info', on_delete=models.CASCADE, null=True,db_column='apartment')
    # 财产名称
    Pname = models.CharField(max_length=35,db_column='financial name')
    # 财产价格
    Pprice = models.IntegerField(db_column='price')
    # 财产数量
    Pnum = models.IntegerField(db_column='number')
    # 搬入时间
    Pintime = models.DateField(db_column='move in time')
    # 搬出时间
    Pouttime = models.DateField(blank=True, null=True,db_column='move out time')

    class Meta:
        verbose_name_plural = "财务信息"
    def __str__(self):
        return '{} {}'.format(self.Aapart, self.Pname)


# noinspection PyUnusedLocal
@receiver(pre_delete, sender=Student_info)
def pre_delete_student(sender, instance, **kwargs):
    Aroom = instance.Aroom
    Aroom.exists -= 1
    Aroom.save()

# noinspection PyUnusedLocal
@receiver(pre_save, sender=Student_info)
def pre_save_student(sender, instance, **kwargs):
    if instance.Sid:
        old_grade = Student_info.objects.get(Sid=instance.Sid).Aroom
        new_grade = instance.Aroom
        if old_grade.Rroom != new_grade.Rroom:
            old_grade.exists -= 1
            new_grade.exists += 1
            old_grade.save()
            new_grade.save()
    elif instance.Sid:
        Aroom = instance.Aroom
        Aroom.exists += 1
        Aroom.save()
