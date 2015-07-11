from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import Http404

# Create your views here.

def html_view(request,html_id):
	html_file = None
	try:
		html_file = open(settings.HTML_FILES+'html'+str(html_id)+'.html' ,'rt',encoding='utf-8')
		content = html_file.readlines()
	except Exception as err:
		raise Http404
	finally:
		if (html_file is not None):
			html_file.close()

	return HttpResponse(content)