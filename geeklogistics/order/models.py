#-*- coding:utf-8 -*-

from django.db import models

class Order(models.Model):
	order_id = models.CharField('订单编号', max_length=30)
	deliver_id = models.CharField('配送编号', max_length=50)
	poi_id = models.CharField('商家id', max_length=30)
	current_location = models.CharField('当前位置id', max_length=60)
	ctime = models.DateField('订单创建时间', max_length=30)
	utime = models.DateField('订单最新修改时间', max_length=30)
	status = models.CharField('订单状态', max_length=3)

	class Meta:
		verbose_name = '订单'
		verbose_name_plural = '订单'

	def __unicode__(self):
		return self.order_id