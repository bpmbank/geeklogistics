# -*- coding:utf-8 -*-

from datetime import datetime

from django.db import models

WORKSTATUS_CHOICES = (
    ('0', '工作中'),
    ('1', '休假中'),
)


class Dispatcher(models.Model):
    dispatcher_id = models.CharField('编号', max_length=20)
    name = models.CharField('姓名', max_length=30)
    password = models.CharField('密码', max_length=30, default="123456")
    work_status = models.CharField('配送员当前状态', max_length=30, choices=WORKSTATUS_CHOICES)  # 可选状态
    phone = models.CharField('手机', max_length=30)
    photo = models.ImageField('配送员照片', max_length=100, upload_to='static/images/dispatcher/', null=True, blank=True)
    ctime = models.DateTimeField('创建时间', max_length=30, default=datetime.now())
    utime = models.DateTimeField('最新修改时间', max_length=30, default=datetime.now())
    status = models.CharField('状态', max_length=3, default=0)

    class Meta:
        verbose_name = '配送员'
        verbose_name_plural = '配送员'

    def as_json(self):
        return dict(
            id=self.id, dispatcher_id=self.dispatcher_id, name=self.name,
            work_status=self.work_status, phone=self.phone, photo=str(self.photo)
        )

    def __unicode__(self):
        return self.dispatcher_id


class Driver(models.Model):
    driver_id = models.CharField('编号', max_length=20)
    name = models.CharField('姓名', max_length=30)
    password = models.CharField('密码', max_length=30, default="abcd1234")
    work_status = models.CharField('司机当前状态', max_length=30, choices=WORKSTATUS_CHOICES)  # 可选状态
    phone = models.CharField('手机', max_length=30)
    photo = models.ImageField('司机照片', max_length=60, upload_to='static/images/driver/', null=True, blank=True)
    ctime = models.DateTimeField('创建时间', max_length=30, default=datetime.now())
    utime = models.DateTimeField('最新修改时间', max_length=30, default=datetime.now())
    status = models.CharField('状态', max_length=3, default=0)

    class Meta:
        verbose_name = '司机'
        verbose_name_plural = '司机'

    def as_json(self):
        return dict(
            id=self.id, driver_id=self.driver_id, name=self.name,
            work_status=self.work_status, phone=self.phone, photo=str(self.photo)
        )

    def __unicode__(self):
        return self.driver_id
