#-*- coding:utf-8 -*-

from datetime import datetime
from django.db import models
from geeklogistics.poi.models import Merchant
from geeklogistics.deliver.models import Dispatcher
from geeklogistics.station.models import Station
from django.forms import ModelForm

ORDER_STATUS_CHOICES = (
	('0', '未下单'),
	('100', '已下单'),
	('200', '已取货'),
	('300', '运输中'),
	('400', '开始配送'),
	('500', '已配送'),
	('600', '已完成'),
	('700', '已取消'),
)

class Detail(models.Model):
	PAY_CHOICES = (
		('0', '否'),
		('1', '是'),
	)
	order_id = models.CharField('订单编号', max_length=30, null=True, blank=True)
	phone = models.CharField('订单联系人电话', max_length=20)
	stuff = models.CharField('需要被配送物件', max_length=200, null=True, blank=True)  #todo 每个物件价格，名称
	name = models.CharField('发货人姓名', max_length=20)
	address = models.CharField('取货地址', max_length=200)
	customer_name = models.CharField('收货人姓名', max_length=20)
	customer_phone = models.CharField('收货人电话', max_length=20)
	customer_address = models.CharField('收货人地址', max_length=30)
	total_price = models.FloatField('订单总价', null=True, blank=True)
	to_pay = models.CharField('是否需要代收款', max_length=3, default=0, choices=PAY_CHOICES)

	def __unicode__(self):
		return self.id

class Order(models.Model):
	deliver_id = models.CharField('配送编号', max_length=50, null=True, blank=True)  #规则编号
	poi = models.ForeignKey(Merchant, verbose_name="订单商家", null=True, blank=True)
	start_time = models.DateTimeField(verbose_name="开始配送时间", null=True, blank=True)
	end_time = models.DateTimeField(verbose_name="送达时间", null=True, blank=True)
	order_id = models.CharField('订单编号', max_length=30, null=True, blank=True)	
	order_status = models.CharField('订单状态', max_length=3, default=0, choices=ORDER_STATUS_CHOICES)
	price = models.FloatField('配送价格', default=0)
	order_detail = models.ForeignKey(Detail, verbose_name="订单详情")
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
		deliver_id = self.deliver_id
		order_id = self.order_detail.order_id
		order_stuff = self.order_detail.stuff
		order_price = self.order_detail.total_price
		order_topay = self.order_detail.to_pay
		customer_name = self.order_detail.customer_name
		customer_phone = self.order_detail.customer_phone
		customer_address = self.order_detail.customer_address
		start_time = ''
		end_time = ''
		if self.start_time:
			start_time = self.start_time.isoformat()
		if end_time:
			end_time = self.end_time.isoformat()
		return dict(
			order_id=order_id, deliver_id=deliver_id, order_stuff=order_stuff,
			order_price=order_price, order_topay=order_topay, customer_name=customer_name,
			customer_phone = customer_phone, customer_address=customer_address,
			start_time=start_time, end_time=end_time)

	def __unicode__(self):
		return self.deliver_id

class StatusRecord(models.Model):
	status = models.CharField('订单状态', max_length=3, default=0, choices=ORDER_STATUS_CHOICES)
	location = models.ForeignKey(Station, verbose_name="当前配送站", null=True, blank=True)
	time = models.DateTimeField('时间', max_length=30, default=datetime.now())
	operator = models.ForeignKey(Dispatcher, verbose_name="配送员", null=True, blank=True)
	order_id = models.ForeignKey(Order, verbose_name="配送订单数据库id")

	def __unicode__(self):
		return self.status

class OrderForm(ModelForm):
	class Meta:
		model = Detail
		fields = ('name', 'phone', 'stuff', 'total_price', 'customer_name', 'customer_phone', 'customer_address')
		for field in fields:
			try:
				field.widget.attrs['class'] = "invalid"
			except:
				pass