from django.db import models

# Create your models here.
class Vote(models.Model):
	title = models.CharField("Заголовок опроса", max_length = 250)
	text = models.TextField("Текст")

	def __str__(self):
		return self.title
		
class Answer(models.Model):
	text = models.TextField("Текст")
	votes_count = models.IntegerField("Число ответов", default=0)
	vote = models.ForeignKey(Vote)

	def __str__(self):
		return self.text + " (" + str(self.votes_count) + ")"

class User(models.Model):
	host = models.CharField("Хост", max_length = 15)
	token = models.CharField("Токен", null=True, max_length = 50)
	vote = models.ForeignKey(Vote)

	def __str__(self):
		return self.host + ':' + str(self.token)