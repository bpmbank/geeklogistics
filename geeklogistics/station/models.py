#-*- coding:utf-8 -*-

from django.db import models

class Station(models.Model):
	name = models.CharField('配送点名称', max_length=30)
	address = models.CharField('详细地址', max_length=30)
	tel = models.CharField('联系电话', max_length=30)
	ctime = models.DateTimeField('创建时间', max_length=30)
	utime = models.DateTimeField('最新修改时间', max_length=30)
	status = models.CharField('状态', max_length=3)

	class Meta:
		verbose_name = '配送点'
		verbose_name_plural = '配送点'

	def __unicode__(self):
		return self.name
