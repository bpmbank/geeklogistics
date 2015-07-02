#-*- coding:utf-8 -*-

from datetime import datetime
from django.db import models
from geeklogistics.poi.models import Merchant
from geeklogistics.deliver.models import Dispatcher
from geeklogistics.station.models import Station


class Order(models.Model):
	order_id = models.CharField('订单编号', max_length=30)
	deliver_id = models.CharField('配送编号', max_length=50)
	poi = models.OneToOneField(Merchant, verbose_name="订单商家")
	dispatcher = models.OneToOneField(Dispatcher, verbose_name="配送员")
	start_time = models.DateTimeField(verbose_name="开始配送时间")
	end_time = models.DateTimeField(verbose_name="送达时间")
	current_location = models.OneToOneField(Station, verbose_name="当前配送站")
	ctime = models.DateTimeField('订单创建时间', max_length=30, default=datetime.now())
	utime = models.DateTimeField('订单最新修改时间', max_length=30, default=datetime.now())
	status = models.CharField('订单状态', max_length=3, default=0)

	class Meta:
		verbose_name = '订单'
		verbose_name_plural = '订单'

	def __unicode__(self):
		return self.order_id