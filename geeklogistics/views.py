#-*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from geeklogistics.station.models import Station
from geeklogistics.poi.models import Merchant, Show
from geeklogistics.news.models import News
from geeklogistics.order.models import Order, Detail, StatusRecord

import json  
import time
import random
from time import strftime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.core import serializers


from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

def home(request):
	js_url = 'index'
	news_list = News.objects.all()
	return render_to_response('index.html', {'current_url': 'index', 'news_list': news_list, 'js_url': js_url})

def intro(request):
	js_url = 'intro'
	news_list = News.objects.all()
	return render_to_response('intro.html', {'current_url': 'intro', 'js_url': js_url, 'news_list': news_list})

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
	return render_to_response('news.html', {'current_url': 'intro', 'news': news}) 

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
	# todo：分页
	reminder = ''
	js_url = 'poi/order_list'
	page = request.GET.get('page')
	try:
		poi = Merchant.objects.get(id=poi_id)
		try:
			orders = Order.objects.filter(poi=poi_id, status='0')
			record_list = [] 
			limit = 20
			paginator = Paginator(orders, limit)  # 实例化一个分页对象
			try:
				orders = paginator.page(page)  # 获取某页对应的记录
			except PageNotAnInteger:  # 如果页码不是个整数
				orders = paginator.page(1)  # 取第一页的记录
			except EmptyPage:  # 如果页码太大，没有相应的记录
				orders = paginator.page(paginator.num_pages)  # 取最后一页的记录

			start_index = orders.start_index()
			print start_index	
			index = 0	
			for order in orders:
				myorder = {} #why必须先初始化？
				myorder['order_id'] = order.order_detail.order_id
				myorder['id'] = order.id
				myorder['deliver_id'] = order.deliver_id
				myorder['status'] = order.get_order_status_display()
				# print order.get_order_status_display()
				myorder['order_status'] = order.order_status
				myorder['start_index'] = start_index+index
				record = StatusRecord.objects.filter(order_id = order.id)
				record_length = len(record)
				if(record_length>0):
					myorder['start_time'] = record[0].ctime.strftime("%Y-%m-%d %H:%M:%S")
					myorder['operator'] = record[record_length-1].get_record_operator()
				else:
					myorder['start_time'] = ''
					myorder['operator'] = {}
				index = index+1	
				record_list.append(myorder)
		except:
			pass
	except ObjectDoesNotExist:
		reminder = "该商户不存在"
	return render_to_response('poi/order_list.html', {'current_url': 'coop', 'order_list': record_list, 'orders':orders, 'js_url': js_url, 'reminder': reminder})

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

def order_detail(request, deliver_id):
	js_url = 'order'
	reminder = ''
	try:
		order = Order.objects.get(deliver_id=deliver_id)
		order_status = StatusRecord.objects.filter(order_id=order.id)
		record_list = []
		for status in order_status:
			record_text = status.record_text()
			record_list.append(record_text)
		# print record_list
		return render_to_response('order_detail.html', {'current_url': 'order', 'js_url': js_url,
			'order': order, 'record_list': record_list})
	except ObjectDoesNotExist:
		reminder = "该订单不存在"
		return render_to_response('order_detail.html', {'current_url': 'order_detail', 'js_url': js_url})


