#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from geeklogistics.station.models import Station
from geeklogistics.order.models import Order, Detail, StatusRecord, OrderForm
from django.db.models import Q

import json  
import time
from time import strftime

from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
@csrf_exempt
def login(request):
	if request.method == 'POST':
		username = request.REQUEST.get('username')
		password = request.REQUEST.get('password')
		response_data = {}

		try:
			poi = Station.objects.get(username=username)
			if poi.password == password:
				response_data['code'] = 0  
				response_data['msg'] = 'ok' 
				mypoi = poi.as_json()
				response_data['data'] = mypoi
			else:
				response_data['code'] = 1 
				response_data['msg'] = '用户名或密码错误' 	
		except ObjectDoesNotExist:
			response_data['code'] = 1 
			response_data['msg'] = '用户名不存在'	

		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		js_url = 'station/login'
		return render_to_response('station/login.html', {'current_url': 'coop', 'js_url': js_url})

def order_list(request, station_id):
	# todo：分页
	reminder = ''
	js_url = 'station/order_list'
	try:
		station = Station.objects.get(id=station_id)
		page = request.GET.get('page')
		start_index = 0
		try:
			orders = Order.objects.filter(Q(order_status=0, poi_nearest=station_id) | Q(order_status=100, poi_nearest=station_id))
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
			# todo:
			# 分页count		
		except:
			pass
	except ObjectDoesNotExist:
		reminder = "该配送站不存在"
	return render_to_response('station/order_list.html', {'current_url': 'area',  'orders': orders, 'start_index':start_index, 'js_url': js_url, 'reminder': reminder})

