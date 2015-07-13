#-*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from geeklogistics.station.models import Station
from geeklogistics.poi.models import Merchant, Show
from geeklogistics.news.models import News
from geeklogistics.order.models import Order, OrderForm

import json  
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

def home(request):
	news_list = News.objects.all()
	return render_to_response('index.html', {'current_url': 'index', 'news_list': news_list})

def intro(request):
	return render_to_response('intro.html', {'current_url': 'intro'})

def coop(request):
	return render_to_response('coop.html', {'current_url': 'coop'})

def custom(request):
	customer_list = Show.objects.all()
	print customer_list
	return render_to_response('custom.html', {'current_url': 'custom', 
											'customer_list': customer_list})
def news(request, id):
	news = News.objects.get(id=id) 
	return render_to_response('news.html', {'news': news}) 

def area(request):
	area_list = Station.objects.all()
	print len(area_list)
	return render_to_response('area.html', {'current_url': 'area', 
											'area_list' : area_list})

def order(request):
	return render_to_response('order.html', {'current_url': 'order'})

def list(request, poi_id):
	try:
		poi = Merchant.objects.get(id=poi_id)
		orders = Order.objects.filter(poi=poi_id)
		reminder = ''
		print orders
	except ObjectDoesNotExist:
		reminder = "该商户不存在"
	return render_to_response('list.html', {'current_url': 'coop', 'order_list': orders, 'reminder': reminder})


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

@csrf_exempt
def poi_login(request):
	username = request.POST['username']
	password = request.POST['password']
	response_data = {}

	try:
		poi = Merchant.objects.get(username=username)
		if poi.password == password:
			response_data['code'] = 0  
			response_data['msg'] = 'ok' 
			response_data['poi'] = poi.id	
		else:
			response_data['code'] = 1 
			response_data['msg'] = '用户名或密码错误' 	
	except ObjectDoesNotExist:
		response_data['code'] = 1 
		response_data['msg'] = '用户名不存在'	

	return HttpResponse(json.dumps(response_data), content_type="application/json")  


def order_detail(request, deliver_id):
	try:
		order = Order.objects.get(deliver_id=deliver_id)
		reminder = ''
		print orders
		return render_to_response('order_detail.html', {'current_url': 'order', 'order': order})
	except ObjectDoesNotExist:
		reminder = "该订单不存在"
		return render_to_response('order_detail.html', {'current_url': 'order_detail'})

	order = Order.objects.get(deliver_id=deliver_id)

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
