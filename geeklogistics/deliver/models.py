#-*- coding:utf-8 -*-

from django.db import models

class Dispatcher(models.Model):
	dispatcher_id = models.CharField('编号', max_length=30)
	name = models.CharField('姓名', max_length=30)
	password = models.CharField('密码', max_length=30)
	current_location = models.CharField('当前位置id', max_length=30)
	phone = models.CharField('手机', max_length=30)
	photo = models.CharField('照片', max_length=60)
	ctime = models.DateField('创建时间', max_length=30)
	utime = models.DateField('最新修改时间', max_length=30)
	status = models.CharField('状态', max_length=3)

	class Meta:
		verbose_name = '配送员'
		verbose_name_plural = '配送员'

	def __unicode__(self):
		return self.dispatcher_id
