#-*- coding:utf-8 -*-

from django.db import models
from datetime import datetime

class Station(models.Model):
	username = models.CharField('配送点用户名', max_length=30)
	password = models.CharField('配送点密码', max_length=30, default='123456')
	name = models.CharField('配送点名称', max_length=30)
	address = models.CharField('详细地址', max_length=50)
	phone = models.CharField('联系电话', max_length=30, default='400-8870-387',null=True, blank=True)
	latitude = models.FloatField('纬度', default=0)
	longitude = models.FloatField('经度', default=0)
	image = models.ImageField('站点图片', max_length=100, upload_to='static/images/station/', null=True, blank=True)
	ctime = models.DateTimeField('创建时间', max_length=30, default=datetime.now())
	utime = models.DateTimeField('最新修改时间', max_length=30, default=datetime.now())
	status = models.CharField('状态', max_length=3, default=0)

	class Meta:
		verbose_name = '配送点'
		verbose_name_plural = '配送点'

	def __unicode__(self):
		return self.name
