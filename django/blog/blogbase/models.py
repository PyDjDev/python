from django.db import models

# Create your models here.

class BlogPost(models.Model):
	# id by default
	title = models.CharField("Заголовок поста", max_length=250)
	pud_date = models.DateTimeField("Дата публикации", auto_now = False)
	body = models.TextField("Текст")

	def __str(self):
		return 'Blog post: ' + self.title