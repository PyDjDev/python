from datetime import datetime
from blog.settings import BLOG_FILE

class BlogPost:
	def  __init__(self):
		self.id = 0
		self.title = ""
		self.pub_time = datetime(1,1,1)
		self.body = ""
	
	def __str__(self):
		return "Blog post #{}: {} {} ({})".format(self.id, self.title, self.pub_time.strftime("%x %X"), self.body)

def readBlogPosts():	
	filename = BLOG_FILE
	result = []
	f = None
	try:
		f = open(filename,'r',encoding='utf-8')

		while True:
			b = BlogPost()
			
			b.title = f.readline()
			if len(b.title) == 0:
				break
			b.title = b.title[0:-1]
			
			timestr = f.readline()
			if(len(timestr) == 0):
				break
			try:
				b.pub_time = datetime.strptime(timestr[0:-1],"%Y-%m-%d %H:%M")
			except ValueError:
				pass
			
			s = f.readline()
			while (len(s) > 0):
				#s = s[0:-1]
				if s == ".\n":
					break
				b.body += s
				s = f.readline()
			
			b.id = len(result)
			
			result.append(b)
		#TODO sorted
		return result
	except OSError as e:
		print("Exception: OSError({})".format(repr(e.args)))
		return []
	finally:
		if f is not None:
			f.close()