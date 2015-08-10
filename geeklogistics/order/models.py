# coding:utf-8
# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from geeklogistics.poi.models import Merchant
from geeklogistics.deliver.models import Dispatcher, Driver
from geeklogistics.station.models import Station
from django.forms import ModelForm

ORDER_STATUS_CHOICES = (
    (0, '未下单'),
    (100, '已下单'),
    (200, '已取货'),
    (300, '运输中'),
    (400, '开始配送'),
    (500, '已配送'),
    (600, '已完成'),
    (700, '已取消'),
    (800, '已拒收'),
)


class Detail(models.Model):
    PAY_CHOICES = (
        ('0', '否'),
        ('1', '是'),
    )
    # todo
    # 备注
    order_id = models.CharField('订单编号', max_length=30, null=True, blank=True)
    phone = models.CharField('订单联系人电话', max_length=20)
    stuff = models.CharField('需要被配送物件', max_length=200, null=True, blank=True)  # todo 每个物件价格，名称
    name = models.CharField('发货人姓名', max_length=20)
    address = models.CharField('取货地址', max_length=200)
    customer_name = models.CharField('收货人姓名', max_length=20)
    customer_phone = models.CharField('收货人电话', max_length=20)
    customer_address = models.CharField('收货人地址', max_length=200)
    remark = models.CharField('订单备注', max_length=200, null=True, blank=True)
    total_price = models.FloatField('订单总价', null=True, blank=True)
    to_pay = models.CharField('是否需要代收款', max_length=3, default=0, choices=PAY_CHOICES)

    def __unicode__(self):
        return self.id


class Order(models.Model):
    DSTATUS_CHOICES = (
        ('0', '正常'),
        ('1', '已删除'),
    )
    deliver_id = models.CharField('配送编号', max_length=50, null=True, blank=True)  # 规则编号
    poi = models.ForeignKey(Merchant, verbose_name="订单商家", null=True, blank=True)
    start_time = models.DateTimeField(verbose_name="开始配送时间", null=True, blank=True)
    end_time = models.DateTimeField(verbose_name="送达时间", null=True, blank=True)
    order_id = models.CharField('订单编号', max_length=30, null=True, blank=True)
    order_status = models.IntegerField('订单状态', default=0, choices=ORDER_STATUS_CHOICES)
    poi_nearest = models.ForeignKey(Station, verbose_name="商家最近取货站点", related_name='商家最近取货站点+', null=True, blank=True)
    customer_nearest = models.ForeignKey(Station, verbose_name="收货人最近站店", related_name='收货人最近站店+', null=True,
                                         blank=True)
    price = models.FloatField('配送价格', default=20)
    order_detail = models.ForeignKey(Detail, verbose_name="订单详情")
    order_type = models.CharField('状态', max_length=3, default=0)
    ctime = models.DateTimeField('订单创建时间', max_length=30, default=datetime.now())
    utime = models.DateTimeField('订单最新修改时间', max_length=30, default=datetime.now())
    status = models.CharField('状态', max_length=3, default=0, choices=DSTATUS_CHOICES)

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
        customer_nearest = self.customer_nearest.name
        order_status = self.order_status
        start_time = ''
        end_time = ''
        if self.start_time:
            start_time = self.start_time.isoformat()
        if end_time:
            end_time = self.end_time.isoformat()
        return dict(
            id=self.id, order_id=order_id, deliver_id=deliver_id, order_stuff=order_stuff,
            order_price=order_price, order_topay=order_topay, customer_name=customer_name,
            customer_phone=customer_phone, customer_address=customer_address,
            start_time=start_time, end_time=end_time, status=order_status, customer_nearest=customer_nearest)

    def __unicode__(self):
        return self.deliver_id


class StatusRecord(models.Model):
	OPERATOR_TYPE_CHOICES = (
		('0', '分拣站'),
		('1', '配送员'),
		('2', '司机'),
	)
	# todo status改int型
	status = models.IntegerField('订单状态', default=0, choices=ORDER_STATUS_CHOICES)
	ctime = models.DateTimeField('时间', max_length=30, default=datetime.now())
	operator_type = models.CharField('操作人类型', max_length=3, default=0, choices=OPERATOR_TYPE_CHOICES)
	operator_id = models.IntegerField(verbose_name="操作人对应id", null=True, blank=True)
	reject_reason = models.CharField(verbose_name="拒收理由", max_length=300, null=True, blank=True)
	order = models.ForeignKey(Order, verbose_name="配送订单数据库id")
	receiver_name = models.CharField('真实收货人', max_length=80, default='', null=True, blank=True)

	def __unicode__(self):
		return self.status

	def get_record_operator(self):
		if self.operator_type == '0':
			operator = Station.objects.get(id=self.operator_id)
		elif self.operator_type == '1':
			operator = Dispatcher.objects.get(id=self.operator_id)
		elif self.operator_type == '2':
			operator = Driver.objects.get(id = self.operator_id)

		return operator		

	def record_text(self):
		text = ''
		time_format = self.ctime.strftime("%Y-%m-%d %H:%M:%S")
		if self.operator_type == '0':
			operator = Station.objects.get(id=self.operator_id)
		elif self.operator_type == '1':
			operator = Dispatcher.objects.get(id=self.operator_id)
		elif self.operator_type == '2':
			operator = Driver.objects.get(id = self.operator_id)

		order = Order.objects.get(id=self.order_id)

		# todo：加入出库入库等提示？
		if(self.status == 200):
			text = time_format + ' ' + '配送员 '+ operator.name.encode('utf-8') + '(电话：'+operator.phone.encode('utf-8')+') 已从商家取货';
		elif(self.status == 300):
			if self.operator_type == '0':
				if self.operator_id == 11:
					text = time_format + ' ' + '货物正在分拣站 '+ operator.name.encode('utf-8') + '进行分拣';
				else:
					text = time_format + ' ' + '货物已经到达 '+ operator.name.encode('utf-8');
			elif self.operator_type == '2':
				text = time_format + ' ' + '货物正由司机 '+ operator.name.encode('utf-8') + ' 运往下一站点';				
		elif(self.status == 400):
			text = time_format + ' ' + '货物正由配送员 '+ operator.name.encode('utf-8') + '(电话：'+operator.phone.encode('utf-8')+') 开始配送';
		elif(self.status == 500):
			if self.receiver_name :
				text = time_format + ' ' + '货物已由用户'+self.receiver_name.encode('utf-8')+'签收';
			else:
				text = time_format + ' ' + '货物已由用户'+order.order_detail.customer_name.encode('utf-8')+'签收';
		elif(self.status == 700):
			text = time_format + ' 订单已被取消';			
		elif(self.status == 800):
			text = time_format + ' ' + '货物已被拒收，拒收理由为：'+self.reject_reason.encode('utf-8');			
		return text


class OrderForm(ModelForm):
    class Meta:
        model = Detail
        fields = ('name', 'phone', 'stuff', 'total_price', 'customer_name', 'customer_phone', 'customer_address')
        for field in fields:
            try:
                field.widget.attrs['class'] = "invalid"
            except:
                pass
