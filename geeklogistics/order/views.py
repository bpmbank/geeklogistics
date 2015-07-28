#-*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from geeklogistics.station.models import Station
from geeklogistics.poi.models import Merchant
from geeklogistics.order.models import Order, Detail, StatusRecord, OrderForm

import json  
import time
import random

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

# 获取订单列表ajax
@csrf_exempt
def order_list(request):
	if request.method == 'POST':
		poi_id = request.REQUEST.get('poiId', 0)
		response_data = {}
		try:
			poi = Merchant.objects.get(id=poi_id)
			orders = Order.objects.filter(poi=poi_id)
			response_data['code'] = 0
			response_data['msg'] = 'ok'
			myorderlist = []
			for order in orders:
				myorder = order.as_json()
				try:
					status = StatusRecord.objects.filter(order_id=order.id).latest('id')
				except ObjectDoesNotExist:	
					status = None
				myorder['status'] = status
				myorderlist.append(myorder)
			response_data['data'] = myorderlist
		except ObjectDoesNotExist:
			response_data['code'] = 1 
			response_data['msg'] = '该商户不存在' 
		return HttpResponse(json.dumps(response_data), content_type="application/json")  
