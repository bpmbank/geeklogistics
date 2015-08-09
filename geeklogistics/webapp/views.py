# -*- coding:utf-8 -*-
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from geeklogistics.order.models import Order
from geeklogistics.deliver.models import Dispatcher
from geeklogistics.station.models import Station


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


@csrf_exempt
def dispatcher_login(request):
    if request.method == 'POST':  # 如果表单被提交
        username = request.POST['username']
        password = request.POST['password']
        response_data = {}
        print username, password
        try:
            dispatcher = Dispatcher.objects.get(phone=username)
            print dispatcher.password
            if dispatcher.password == password:
                response_data['code'] = 0
                response_data['msg'] = 'ok'
                response_data['dispatcher'] = dispatcher.id
            else:
                response_data['code'] = 1
                response_data['msg'] = '用户名或密码错误'
        except ObjectDoesNotExist:
            response_data['code'] = 1
            response_data['msg'] = '用户名不存在'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return render_to_response('webapp/express_login.html', {'current_url': 'dispatcher_login'})


def dispatcher_orders(request, dispatcher_id):
    area_list = Station.objects.all()
    try:
        # dispatcher = Dispatcher.objects.get(id=dispatcher_id)
        orders = Order.objects.filter(dispatcher=dispatcher_id)
        reminder = ''
        print orders
    except ObjectDoesNotExist:
        reminder = "该配送员不存在"
    return render_to_response('webapp/express_order_list.html', {'current_url': 'dispatcher_list', 'order_list': orders,
                                                                 'area_list': area_list, 'reminder': reminder})


@csrf_exempt
def location_update(request):
    if request.method == 'POST':  # 如果表单被提交
        order_ids = request.POST['orderIds'].split(',')
        station_id = request.POST['stationId']
        print order_ids, station_id
        response_data = {}
        if (len(order_ids) > 0):
            print "dayu0"
            for order_id in order_ids:
                order = Order.objects.get(id=order_id)
                order.current_location_id = station_id
                # order.update(current_location_id=station_id)
                order.save()
                response_data['code'] = 0
                response_data['msg'] = 'ok'
        else:
            response_data['code'] = 1
            response_data['msg'] = '请选择订单'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
