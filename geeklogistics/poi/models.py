#-*- coding:utf-8 -*-

from django.db import models
from datetime import datetime

class Merchant(models.Model):
	username = models.CharField('商家用户名', max_length=30)
	password = models.CharField('商家登录密码', max_length=30)
	name = models.CharField('商家名称', max_length=30)
	address = models.CharField('商家地址', max_length=50)
	tel = models.CharField('商家电话', max_length=30)
	logo = models.ImageField('商家图标', max_length=50, upload_to='static/images/logo/')
	ctime = models.DateTimeField('创建时间', max_length=30, default=datetime.now())
	utime = models.DateTimeField('最新修改时间', max_length=30, default=datetime.now())
	status = models.CharField('状态', max_length=3, default=0)

	class Meta:
		verbose_name = '商家'
		verbose_name_plural = '商家'

	def __unicode__(self):
		return self.name

class Show(models.Model):
	poi = models.OneToOneField(Merchant, verbose_name="订单商家")

	class Meta:
		verbose_name = '展示商家'
		verbose_name_plural = '展示商家'

	def __unicode__(self):
		return self.poi.name