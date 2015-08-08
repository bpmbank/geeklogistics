#-*- coding:utf-8 -*-
from django.http import HttpResponse
from geeklogistics.deliver.models import Dispatcher, Driver
import json  

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
def dispatcher_login(request):
	if request.method == 'POST':
		username = request.REQUEST.get('username')
		password = request.REQUEST.get('password')
		response_data = {}

		try:
			dispatcher = Dispatcher.objects.get(phone=username)
			if dispatcher.password == password:
				response_data['code'] = 0  
				response_data['msg'] = 'ok' 
				mydispatcher = dispatcher.as_json()
				response_data['data'] = mydispatcher
			else:
				response_data['code'] = 1 
				response_data['msg'] = '用户名或密码错误' 	
		except ObjectDoesNotExist:
			response_data['code'] = 1 
			response_data['msg'] = '用户名不存在'	

		return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def dispatcher_change_password(request):
	if request.method == 'POST':
		username = request.REQUEST.get('username')
		origin_password = request.REQUEST.get('originPassword')
		new_password = request.REQUEST.get('newPassword')

		response_data = {}

		try:
			dispatcher = Dispatcher.objects.get(phone=username)
			if dispatcher.password == origin_password:
				dispatcher.password = new_password
				dispatcher.save()
				response_data['code'] = 0  
				response_data['msg'] = 'ok' 
				response_data['data'] = {}
			else:
				response_data['code'] = 1 
				response_data['msg'] = '用户名或密码错误' 	
		except ObjectDoesNotExist:
			response_data['code'] = 1 
			response_data['msg'] = '用户名不存在'	

		return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def driver_login(request):
	if request.method == 'POST':
		username = request.REQUEST.get('username')
		password = request.REQUEST.get('password')
		response_data = {}

		try:
			dispatcher = Driver.objects.get(phone=username)
			if dispatcher.password == password:
				response_data['code'] = 0  
				response_data['msg'] = 'ok' 
				mydispatcher = dispatcher.as_json()
				response_data['data'] = mydispatcher
			else:
				response_data['code'] = 1 
				response_data['msg'] = '用户名或密码错误' 	
		except ObjectDoesNotExist:
			response_data['code'] = 1 
			response_data['msg'] = '用户名不存在'	

		return HttpResponse(json.dumps(response_data), content_type="application/json")



@csrf_exempt
def driver_change_password(request):
	if request.method == 'POST':
		username = request.REQUEST.get('username')
		origin_password = request.REQUEST.get('originPassword')
		new_password = request.REQUEST.get('newPassword')

		response_data = {}

		try:
			dispatcher = Driver.objects.get(phone=username)
			if dispatcher.password == origin_password:
				dispatcher.password = new_password
				dispatcher.save()
				response_data['code'] = 0  
				response_data['msg'] = 'ok' 
				response_data['data'] = {}
			else:
				response_data['code'] = 1 
				response_data['msg'] = '用户名或密码错误' 	
		except ObjectDoesNotExist:
			response_data['code'] = 1 
			response_data['msg'] = '用户名不存在'	

		return HttpResponse(json.dumps(response_data), content_type="application/json")
