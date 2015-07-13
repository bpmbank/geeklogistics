#-*- coding:utf-8 -*-

from datetime import datetime
from django.db import models
from geeklogistics.poi.models import Merchant
from geeklogistics.deliver.models import Dispatcher
from geeklogistics.station.models import Station
from django.forms import ModelForm

class Detail(models.Model):
	phone = models.CharField('订单联系人电话', max_length=20)
	stuff = models.CharField('需要被配送物件', max_length=200)  #todo 每个物件价格，名称
	name = models.CharField('发货人姓名', max_length=20)
	customer_name = models.CharField('收货人姓名', max_length=20)
	customer_phone = models.CharField('收货人电话', max_length=20)
	customer_address = models.CharField('收货人地址', max_length=30)
	total_price = models.FloatField('订单总价')

	def __unicode__(self):
		return self.id

class Order(models.Model):
	ORDER_CHOICES = (
		('0', '未配送'),
		('1', '配送中'),
	)
	order_id = models.CharField('订单编号', max_length=30, null=True, blank=True)
	deliver_id = models.CharField('配送编号', max_length=50, null=True, blank=True)  #规则编号
	poi = models.OneToOneField(Merchant, verbose_name="订单商家", null=True, blank=True)
	dispatcher = models.OneToOneField(Dispatcher, verbose_name="配送员", null=True, blank=True)
	start_time = models.DateTimeField(verbose_name="开始配送时间", null=True, blank=True)
	end_time = models.DateTimeField(verbose_name="送达时间", null=True, blank=True)
	current_location = models.OneToOneField(Station, verbose_name="当前配送站", null=True, blank=True)
	order_status = models.CharField('订单状态', max_length=3, default=0, choices=ORDER_CHOICES)
	price = models.FloatField('配送价格', default=0)
	order_detail = models.OneToOneField(Detail, verbose_name="订单详情")
	order_type = models.CharField('状态', max_length=3, default=0)
	ctime = models.DateTimeField('订单创建时间', max_length=30, default=datetime.now())
	utime = models.DateTimeField('订单最新修改时间', max_length=30, default=datetime.now())
	status = models.CharField('状态', max_length=3, default=0)

	# todo 操作记录表，处理人，处理事件，订单号，
	# todo 节假日不配送订单开关，单独配置，可以推送到系统，可能要几日后配送,
	# todo 订单分配给配送员，多选，单选
	class Meta:
		verbose_name = '订单'
		verbose_name_plural = '订单'
		# proxy = True

	def as_json(self):
		return dict(
			order_id=self.order_id,deliver_id=self.deliver_id, 
			poi=self.poi.name, dispatcher=self.dispatcher.name, 
			start_time=self.start_time.isoformat(), end_time=self.end_time.isoformat(), 
			current_location=self.current_location.name)

	def __unicode__(self):
		return self.order_id

class OrderForm(ModelForm):
	class Meta:
		model = Detail
		fields = ('name', 'phone', 'stuff', 'total_price', 'customer_name', 'customer_phone', 'customer_address')
		for field in fields:
			try:
				field.widget.attrs['class'] = "invalid"
			except:
				pass