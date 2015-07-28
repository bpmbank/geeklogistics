#-*- coding:utf-8 -*-

from django.db import models
from datetime import datetime

class Dispatcher(models.Model):
	WORKSTATUS_CHOICES = (
		('0', '可以接单配送'),
		('1', '正在配送中'),
		('2', '休假中'),
	)
	TYPE_CHOICES = (
		('0', '配送员'),
		('1', '分拣员'),
	)

	dispatcher_id = models.CharField('编号', max_length=20)
	name = models.CharField('姓名', max_length=30)
	password = models.CharField('密码', max_length=30, default="abcd1234")
	current_location = models.CharField('当前位置id', max_length=30, default=0)  #暂时不需要
	work_status = models.CharField('配送员当前状态', max_length=30, choices=WORKSTATUS_CHOICES) #可选状态
	dispatcher_type = models.CharField('工种', max_length=3,  default=0, choices=TYPE_CHOICES) #可选状态
	phone = models.CharField('手机', max_length=30)
	photo = models.ImageField('配送员照片', max_length=60, upload_to='static/images/dispatcher/', null=True, blank=True)	
	ctime = models.DateTimeField('创建时间', max_length=30, default=datetime.now())
	utime = models.DateTimeField('最新修改时间', max_length=30, default=datetime.now())
	status = models.CharField('状态', max_length=3, default=0)

	class Meta:
		verbose_name = '配送员'
		verbose_name_plural = '配送员'

	def __unicode__(self):
		return self.dispatcher_id
