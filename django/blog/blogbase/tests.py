from django.test import TestCase
from blogbase.blogdata import readBlogPosts
# Create your tests here.

def readBlogs():
	for i in readBlogPosts():
		print(i)