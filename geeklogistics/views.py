#-*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from geeklogistics.station.models import Station
from geeklogistics.poi.models import Merchant, Show
from geeklogistics.news.models import News
from geeklogistics.order.models import Order, Detail, StatusRecord, OrderForm

import json  
import time
import random

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.core import serializers

def home(request):
	news_list = News.objects.all()
	return render_to_response('index.html', {'current_url': 'index', 'news_list': news_list})

def intro(request):
	js_url = 'intro'
	return render_to_response('intro.html', {'current_url': 'intro', 'js_url': js_url})

def coop(request):
	js_url = 'coop'
	return render_to_response('poi/login.html', {'current_url': 'coop', 'js_url': js_url})

def poi_apply(request):
	return render_to_response('poi/apply.html', {'current_url': 'coop'})

def custom(request):
	customer_list = Show.objects.all()
	return render_to_response('custom.html', {'current_url': 'custom', 
											'customer_list': customer_list})
def news(request, id):
	news = News.objects.get(id=id) 
	return render_to_response('news.html', {'news': news}) 

def area(request):
	area_list = Station.objects.all()
	js_url = 'area'
	return render_to_response('area.html', {'current_url': 'area', 'js_url': js_url,
											'area_list' : area_list})

def order(request):
	js_url = 'order'
	return render_to_response('order.html', {'current_url': 'order', 'js_url': js_url})

def order_success(request, deliver_id):
	poi_id = request.COOKIES.get('poiid')
	deliver_id = deliver_id
	return render_to_response('poi/order_success.html', {'current_url': 'coop', 'poi_id': poi_id, 'deliver_id': deliver_id})

def list(request, poi_id):
	try:
		poi = Merchant.objects.get(id=poi_id)
		print poi_id
		orders = Order.objects.filter(poi=poi_id)
		print orders
		reminder = ''
	except ObjectDoesNotExist:
		reminder = "该商户不存在"
	js_url = 'poi/order_list'
	return render_to_response('poi/order_list.html', {'current_url': 'coop', 'order_list': orders, 'js_url': js_url, 'reminder': reminder})



# 商家手动下单页面
@csrf_exempt
def poi_order(request):
	reminder = ''
	js_url = 'poi/order'
	poi_id = request.COOKIES.get('poiid')
	try:
		poi = Merchant.objects.get(id=poi_id)
	except ObjectDoesNotExist:
		reminder = "该商户不存在"
	return render_to_response('poi/order.html', {'current_url': 'coop', 'js_url': js_url, 'poi': poi, 'reminder': reminder})

@csrf_exempt
def order_detail_ajax(request):
	deliver_id = request.POST['deliverId']
	order = Order.objects.get(deliver_id=deliver_id).as_json()
	response_data = {}  
	if(order):
		response_data['code'] = 0  
		response_data['msg'] = 'ok' 
		response_data['order'] = order  
	else:
		response_data['code'] = 1 
		response_data['msg'] = '没有查到相关订单' 

	return HttpResponse(json.dumps(response_data), content_type="application/json")  
  

def order_detail(request, deliver_id):
	js_url = 'order'
	try:
		order = Order.objects.get(deliver_id=deliver_id)
		order_status = StatusRecord.objects.filter(order_id=order.id)
		record_list = []
		for status in order_status:
			record_text = status.record_text()
			record_list.append(record_text)
		print record_list
		reminder = ''
		return render_to_response('order_detail.html', {'current_url': 'order', 'js_url': js_url,
			'order': order, 'record_list': record_list})
	except ObjectDoesNotExist:
		reminder = "该订单不存在"
		return render_to_response('order_detail.html', {'current_url': 'order_detail', 'js_url': js_url})

@csrf_exempt
def order_new(request):
	if request.method == 'POST': # 如果表单被提交
		form = OrderForm(request.POST) # 获取Post表单数据
		if form.is_valid(): # 验证表单
			detail = form.save()
			print detail.id
			detail_id = detail.id
			order = Order(order_detail_id=detail_id)
			order.save()
			return HttpResponseRedirect('/') # 跳转
			# return render_to_response('send.html', {'form': form,})
			# return render_to_response('send.html', {'form': form,}, context_instance=RequestContext(request))
		else:
			return render_to_response('send.html', {'form': form,}, context_instance=RequestContext(request))
	else:
		form = OrderForm() #获得表单对象
		return render_to_response('send.html', {'form': form,})
