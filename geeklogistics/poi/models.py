#-*- coding:utf-8 -*-

from django.db import models

class Merchant(models.Model):
	username = models.CharField('商家用户名', max_length=30)
	password = models.CharField('商家登录密码', max_length=30)
	name = models.CharField('商家名称', max_length=30)
	address = models.CharField('商家地址', max_length=50)
	tel = models.CharField('商家电话', max_length=30)
	logo = models.CharField('商家图标', max_length=50)
	ctime = models.DateField('创建时间', max_length=30)
	utime = models.DateField('最新修改时间', max_length=30)
	status = models.CharField('状态', max_length=3)

	class Meta:
		verbose_name = '商家'
		verbose_name_plural = '商家'

	def __unicode__(self):
		return self.id
