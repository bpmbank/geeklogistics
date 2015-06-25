from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(request):
	return render_to_response('index.html', {'current_url': 'index'})

def intro(request):
	return render_to_response('intro.html', {'current_url': 'intro'})

def coop(request):
	return render_to_response('coop.html', {'current_url': 'coop'})

def custom(request):
	return render_to_response('custom.html', {'current_url': 'custom'})

def area(request):
	return render_to_response('area.html', {'current_url': 'area'})

def order(request):
	return render_to_response('order.html', {'current_url': 'order'})

def list(request):
	return render_to_response('list.html', {'current_url': 'coop'})
