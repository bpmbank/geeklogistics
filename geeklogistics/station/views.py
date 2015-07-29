#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from geeklogistics.station.models import Station
from geeklogistics.order.models import Order, Detail, StatusRecord, OrderForm

import json  
import time
from time import strftime

from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

