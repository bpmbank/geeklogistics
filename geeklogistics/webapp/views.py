#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from geeklogistics.order.models import Order, OrderForm

def home(request):
	return render_to_response('webapp/index.html', {'current_url': 'index'})

def intro(request):
	return render_to_response('webapp/introduction.html', {'current_url': 'intro'})

def news(request):
	return render_to_response('webapp/news.html', {'current_url': 'news'})

def service(request):
	return render_to_response('webapp/service.html', {'current_url': 'service'})

def contact(request):
	return render_to_response('webapp/contact_us.html', {'current_url': 'contact'})

def order_search(request):
	return render_to_response('webapp/order_search.html', {'current_url': 'order_search'})

def order_result(request, deliver_id):
	try:
		order = Order.objects.get(deliver_id=deliver_id)
		reminder = ''
		print order
		return render_to_response('webapp/order_search_result.html', {'current_url': 'order_detail', 'order': order})
	except ObjectDoesNotExist:
		reminder = "该订单不存在"
		return render_to_response('webapp/order_search_result.html', {'current_url': 'order_detail'})

def merchant_login(request):
	return render_to_response('webapp/merchant_login.html', {'current_url': 'merchant_login'})

def dispatcher_login(request):
	return render_to_response('webapp/express_login.html', {'current_url': 'express_login'})
