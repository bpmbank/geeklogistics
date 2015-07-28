#-*- coding:utf-8 -*-
from django.http import HttpResponse
from geeklogistics.poi.models import Merchant
import json  

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
def poi_login(request):
	if request.method == 'POST':
		username = request.REQUEST.get('username')
		password = request.REQUEST.get('password')
		response_data = {}

		try:
			poi = Merchant.objects.get(username=username)
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