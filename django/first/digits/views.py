from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_page(request):
	return HttpResponse("""
		<!DOCTYPE HTML>
		<html>
			<head><title>Digits</title><meta charset="utf-8"/></head>
			<body>
			<h1>Hellow world</h1>
			<p>We can sum number. Example: <a href="sum/2/3">2 + 3</p>
			</body>			
		</html>""")

def sum_page(request, a, b):
	r = int(a) + int(b)
	return HttpResponse("<h1>Sum of {} and {} is {}.</h1>".format(a,b,r))