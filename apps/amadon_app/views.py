# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'amadon_app/index.html')

def buy(request):
	if request.POST['product_id'] == "1":
		curCost = 19.99 * float(request.POST['quantity'])
	elif request.POST['product_id'] == "2":
		curCost = 29.99 * float(request.POST['quantity'])
	elif request.POST['product_id'] == "3":
		curCost = 4.99 * float(request.POST['quantity'])
	elif request.POST['product_id'] == "4":
		curCost = 49.99 * float(request.POST['quantity'])

	request.session['curCost'] = curCost
	request.session['curCount'] = request.POST['quantity']

	if 'totCost' not in request.session:
		request.session['totCost'] = curCost
	else:
		request.session['totCost'] += curCost

	if 'totCount' not in request.session:
		request.session['totCount'] = int(request.POST['quantity'])
	else:
		request.session['totCount'] += int(request.POST['quantity'])

	return redirect('/amadon/checkout')

def checkout(request):
	return render(request, 'amadon_app/checkout.html')

def clear(request):
	request.session.clear()
	return redirect('/amadon')