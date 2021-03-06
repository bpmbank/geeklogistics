# -*- coding:utf-8 -*-

import json
import urllib2
import time
import random
from math import sin, cos, sqrt, atan2, radians
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from geeklogistics.station.models import Station
from geeklogistics.poi.models import Merchant
from geeklogistics.order.models import Order, Detail, StatusRecord
from django.db.models import Q
import xlrd
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

ORDER_STATUS = {'initial': 0, 'ordered': 100, 'get_order': 200, 'shipping': 300,
                'delivering': 400, 'delivered': 500, 'complete': 600, 'cancel': 700,
                'reject': 800}


# 获取订单列表ajax
# todo：只获取当日的？
@csrf_exempt
def order_list(request):
    if request.method == 'POST':
        poi_id = request.REQUEST.get('poiId', 0)
        status = request.REQUEST.get('status', -1)
        page_size = int(request.REQUEST.get('pageSize', 20))
        current_page = int(request.REQUEST.get('currentPage', 1))
        total_count = int(request.REQUEST.get('totalCount', -1))

        # print status
        response_data = {}
        try:
            orders = []
            poi = Merchant.objects.get(id=poi_id)
            if status == -1:
                orders = Order.objects.filter(poi=poi_id, status='0')
            else:
                if status == '10':
                    # 分页加载数据
                    if total_count <= 0:
                        total_count = Order.objects.filter(
                            Q(order_status=0, poi=poi_id, status='0') | Q(order_status=100, poi=poi_id,
                                                                          status='0')).count()
                    if current_page * page_size >= total_count:
                        end_position = total_count
                    else:
                        end_position = current_page * page_size

                    start_position = (current_page - 1) * page_size
                    orders = Order.objects.filter(
                        Q(order_status=0, poi=poi_id, status='0') | Q(order_status=100, poi=poi_id, status='0'))[
                             start_position:end_position]
                # print orders
                elif status == '20':
                    # 分页加载数据
                    if total_count <= 0:
                        total_count = Order.objects.filter(
                            Q(order_status=200, poi=poi_id, status='0') | Q(order_status=300, poi=poi_id,
                                                                            status='0') | Q(order_status=400,
                                                                                            poi=poi_id,
                                                                                            status='0')).count()
                    if current_page * page_size >= total_count:
                        end_position = total_count
                    else:
                        end_position = current_page * page_size

                    start_position = (current_page - 1) * page_size
                    orders = Order.objects.filter(
                        Q(order_status=200, poi=poi_id, status='0') | Q(order_status=300, poi=poi_id, status='0') | Q(
                            order_status=400, poi=poi_id, status='0'))[start_position:end_position]
                elif status == '30':
                    # 分页加载数据
                    if total_count <= 0:
                        total_count = Order.objects.filter(
                            Q(order_status=500, poi=poi_id, status='0') | Q(order_status=600, poi=poi_id,
                                                                            status='0')).count()
                    if current_page * page_size >= total_count:
                        end_position = total_count
                    else:
                        end_position = current_page * page_size

                    start_position = (current_page - 1) * page_size
                    orders = Order.objects.filter(
                        Q(order_status=500, poi=poi_id, status='0') | Q(order_status=600, poi=poi_id, status='0'))[
                             start_position:end_position]
                elif status == '40':
                    if total_count <= 0:
                        total_count = Order.objects.filter(
                            Q(order_status=700, poi=poi_id, status='0') | Q(order_status=800, poi=poi_id,
                                                                            status='0')).count()
                    if current_page * page_size >= total_count:
                        end_position = total_count
                    else:
                        end_position = current_page * page_size

                    start_position = (current_page - 1) * page_size
                    orders = Order.objects.filter(
                        Q(order_status=700, poi=poi_id, status='0') | Q(order_status=800, poi=poi_id, status='0'))[
                             start_position:end_position]
            response_data['code'] = 0
            response_data['msg'] = 'ok'
            myorderlist = []
            for order in orders:
                myorder = order.as_json()
                myorderlist.append(myorder)
            page_data = {'totalCount': total_count, 'currentPage': current_page, 'pageSize': page_size,
                         'list': myorderlist}
            response_data['data'] = page_data
        except ObjectDoesNotExist:
            response_data['code'] = 1
            response_data['msg'] = '该商户不存在'
        return HttpResponse(json.dumps(response_data), content_type="application/json")


BAIDU_AK = 'GLfzo34AN5Sf7llYeCWlCw8E'


def getLocation(address):
    address = address.encode('utf-8').replace(' ', '')
    baidu_api = 'http://api.map.baidu.com/geocoder/v2/?address=' + address + '&city=北京市&output=json&ak=' + BAIDU_AK
    serialized_data = urllib2.urlopen(baidu_api).read()
    data = json.loads(serialized_data)
    location = data['result']['location']
    return location


# 获取两点距离
def getDistance(lat1, lng1, lat2, lng2):
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lng1)
    lat2 = radians(lat2)
    lon2 = radians(lng2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# 获取最近的配送站
def getNearestStation(location, stations):
    lat = location['lat']
    lng = location['lng']
    nearest_id = 0
    min_distance = 99999999999
    for station in stations:
        tmp_distance = getDistance(lat, lng, station.latitude, station.longitude)
        if tmp_distance < min_distance:
            min_distance = tmp_distance
            nearest_id = station.id
    return nearest_id


def new_order_model(poi_id, poi_name, poi_phone, poi_address, order_id, order_stuff,
                    order_price, order_topay, customer_name, customer_phone, customer_address, remark=''):
    if order_price == '':
        order_price = 0
    # 生成订单详情
    detail = Detail(order_id=order_id, phone=str(poi_phone), name=poi_name, address=poi_address, stuff=order_stuff,
                    customer_name=customer_name, customer_phone=str(customer_phone), customer_address=customer_address,
                    total_price=order_price, to_pay=str(order_topay), remark=remark)
    detail.save()
    poi = Merchant.objects.get(id=poi_id)
    # 生成配送编号
    now = int(time.time())
    randdigit = random.randint(0, 100)
    deliver_id = str(now) + str(randdigit)
    # 生成相关站点
    stations = Station.objects.all()
    # 商家最近 todo:直接关联最近站点
    poi_location = getLocation(poi_address)
    poi_nearest = getNearestStation(poi_location, stations)
    print customer_address + str(poi_nearest)
    # 收货人最近
    customer_location = getLocation(customer_address)
    customer_nearest = getNearestStation(customer_location, stations)
    print customer_address + str(customer_nearest)
    # 插入订单表
    order = Order(deliver_id=deliver_id, poi_id=poi_id, poi_nearest_id=poi_nearest,
                  customer_nearest_id=customer_nearest, order_detail=detail, order_status=ORDER_STATUS['ordered'])
    order.save()

    return order


# 批量倒入订单
@csrf_exempt
def import_order(request):
    response_data = {}
    # print request.FILES
    e_file = request.FILES["orderXls"]
    # print e_file
    poi_id = request.COOKIES.get('poiid', 1)
    poi = Merchant.objects.get(id=poi_id)

    file_test = 'static/excel/order_test.xlsx'
    data = xlrd.open_workbook(file_contents=e_file.read())
    table = data.sheets()[0]
    # 取货地址默认商家已录入地址，如需手动改，修改地址或单独下单或重开账号

    nrows = table.nrows
    for i in range(1, nrows):
        row = table.row_values(i)
        # print table.row_values(i)
        if row[6].encode('utf-8') == '否':
            topay_str = '0'
        else:
            topay_str = '1'
        if row[3].encode('utf-8') != '':
            customer_phone = row[3].encode('utf-8')
        else:
            customer_phone = row[4].encode('utf-8')
        # poi_id, poi_name, poi_phone, poi_address, order_id, order_stuff, order_price, order_topay, 
        # customer_name, customer_phone, customer_address, remark
        new_order_model(poi_id, poi.name, poi.tel, poi.address, str(row[0]), '', row[5], topay_str, row[1],
                        customer_phone, row[2], row[7])
    url = '/list/' + poi_id
    return HttpResponseRedirect(url)


# 下单接口
@csrf_exempt
def order_new(request):
    if request.method == 'POST':  # 如果ajax请求
        response_data = {}
        poi_id = request.REQUEST.get('poiId')
        poi_name = request.REQUEST.get('poiName')
        poi_phone = request.REQUEST.get('poiPhone')
        poi_address = request.REQUEST.get('poiAddress')
        order_stuff = request.REQUEST.get('orderStuff')
        order_id = request.REQUEST.get('orderId')
        order_price = request.REQUEST.get('orderPrice')
        order_remark = request.REQUEST.get('remark', '')
        if order_price == '':
            order_price = 0
        order_topay = request.REQUEST.get('orderTopay')
        customer_name = request.REQUEST.get('customerName')
        customer_phone = request.REQUEST.get('customerPhone')
        customer_address = request.REQUEST.get('customerAddress')
        # 生成订单详情
        detail = Detail(order_id=order_id, phone=poi_phone, name=poi_name, address=poi_address, stuff=order_stuff,
                        customer_name=customer_name, customer_phone=customer_phone, customer_address=customer_address,
                        total_price=order_price, to_pay=order_topay, remark=order_remark)
        detail.save()
        poi = Merchant.objects.get(id=poi_id)
        # 生成配送编号
        now = int(time.time())
        randdigit = random.randint(0, 100)
        deliver_id = str(now) + str(randdigit)
        # 生成相关站点
        stations = Station.objects.all()
        # 商家最近
        poi_location = getLocation(poi_address)
        if poi.nearest_station is None:
            poi_nearest = getNearestStation(poi_location, stations)
        else:
            poi_nearest = poi.nearest_station_id
        # 收货人最近
        customer_location = getLocation(customer_address)
        customer_nearest = getNearestStation(customer_location, stations)
        # 插入订单表
        order = Order(deliver_id=deliver_id, poi_id=poi_id, poi_nearest_id=poi_nearest,
                      customer_nearest_id=customer_nearest, order_detail=detail, order_status=ORDER_STATUS['ordered'])
        order.save()
        response_data['code'] = 0
        response_data['data'] = deliver_id
        return HttpResponse(json.dumps(response_data), content_type="application/json")


# 修改订单状态
@csrf_exempt
def update_order_status(request):
    if request.method == 'POST':  # 如果ajax请求
        response_data = {}
        operator_id = request.REQUEST.get('operatorId')
        operator_type = request.REQUEST.get('operatorType')
        order_status = int(request.REQUEST.get('orderStatus'))
        order_id = int(request.REQUEST.get('orderId', 0))
        station_type = int(request.REQUEST.get('stationType', -1))
        # print order_id
        try:
            if order_id <= 0:
                deliver_id = request.REQUEST.get('deliverId')
                print deliver_id
                order = Order.objects.get(deliver_id=deliver_id)
                order_id = order.id
            else:
                order = Order.objects.get(id=order_id)

            if (int(order_status) < int(order.order_status)) and (order.order_status != 800):
                response_data['code'] = 1
                response_data['msg'] = '系统中订单状态高于需要更改状态'
                response_data['data'] = {}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                # 如果拒收加入拒收理由
                if order_status == ORDER_STATUS['reject']:
                    print 'reject'
                    reject_reason = request.REQUEST.get('rejectReason')
                    record = StatusRecord(status=order_status, order_id=order_id,
                                          operator_type=operator_type, operator_id=operator_id, ctime=datetime.now(),
                                          reject_reason=reject_reason)
                elif order_status == ORDER_STATUS['delivered']:
                    # 如果为确认收货加入真实收货人
                    receiver_name = request.REQUEST.get('receiverName', order.order_detail.customer_name)
                    record = StatusRecord(status=order_status, order_id=order_id, receiver_name=receiver_name,
                                          operator_type=operator_type, operator_id=operator_id, ctime=datetime.now())
                else:
                    record = StatusRecord(status=order_status, order_id=order_id,
                                          operator_type=operator_type, operator_id=operator_id, ctime=datetime.now())
                record.save()
                if (order_status == ORDER_STATUS['get_order']):
                    order.start_time = datetime.now()
                order.order_status = order_status
                order.save()
                return_data = ''
                if station_type == 1:
                    # 如果为总站
                    return_data = order.customer_nearest.name
                response_data['code'] = 0
                response_data['msg'] = 'ok'
                response_data['data'] = return_data
        except ObjectDoesNotExist:
            response_data['code'] = 1
            response_data['msg'] = '该订单不存在，请重新输入'
            response_data['data'] = {}
        except:
            response_data['code'] = 1
            response_data['msg'] = '订单状态更新失败'
            response_data['data'] = {}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

        # 订单详情ajax


@csrf_exempt
def order_detail_ajax(request):
    # deliver_id = request.POST['deliverId']
    db_id = request.REQUEST.get('id')
    order = Order.objects.get(id=db_id).as_json()
    response_data = {}
    if (order):
        response_data['code'] = 0
        response_data['msg'] = 'ok'
        response_data['order'] = order
    else:
        response_data['code'] = 1
        response_data['msg'] = '没有查到相关订单'

    return HttpResponse(json.dumps(response_data), content_type="application/json")


# 删除未配送订单
@csrf_exempt
def order_delete(request):
    if request.method == 'POST':  # 如果ajax请求
        response_data = {}
        order_id = request.REQUEST.get('orderId')
        try:
            order = Order.objects.get(id=order_id)
            order.status = 1;
            order.save()
            response_data['code'] = 0
        except ObjectDoesNotExist:
            response_data['code'] = 1
            response_data['msg'] = '该订单不存在'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        # # modelform

# @csrf_exempt
# def order_new(request):
# 	if request.method == 'POST': # 如果表单被提交
# 		form = OrderForm(request.POST) # 获取Post表单数据
# 		if form.is_valid(): # 验证表单
# 			detail = form.save()
# 			print detail.id
# 			detail_id = detail.id
# 			order = Order(order_detail_id=detail_id)
# 			order.save()
# 			return HttpResponseRedirect('/') # 跳转
# 			# return render_to_response('send.html', {'form': form,})
# 			# return render_to_response('send.html', {'form': form,}, context_instance=RequestContext(request))
# 		else:
# 			return render_to_response('send.html', {'form': form,}, context_instance=RequestContext(request))
# 	else:
# 		form = OrderForm() #获得表单对象
# 		return render_to_response('send.html', {'form': form,})
