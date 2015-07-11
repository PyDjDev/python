from django.shortcuts import render
from django.http import HttpResponse
from blogbase.blogdata import readBlogPosts
from blogbase.models import BlogPost

# Create your views here.

def blog_posts(request):
	context = {
		"pagetitle": 'Blog Post',
		"blog_posts" : BlogPost.objects.all().order_by("-pud_date")
	}
	return render(request,"index.html",context)

def post(request,id):
	context = {
		"pagetitle": 'Post_' + id,
		"post" : BlogPost.objects.get(id=id)
	}
	return render(request,"post.html",context)

'''
	render(request,"templ_name",{dict: ...})
	pipes - {{var| first}} take first element from var
	 		- {{ var | escape}} - transfer to right html
	 		- {{ n | filesizeFormat}} - like 1024 to 1 Kb
	 		- {{ var | default "var1"}} if var is False then var1
'''