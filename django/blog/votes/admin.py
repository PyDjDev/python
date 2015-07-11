from django.contrib import admin

# Register your models here.
from votes.models import Vote, Answer, User

class UserAdmin(admin.StackedInline):
	model = User
	extra = 1
	readonly_fields = ('token',)

class AnswerAdmin(admin.StackedInline):
	model = Answer
	extra = 1
	readonly_fields = ('votes_count',)

class VoteAdmin(admin.ModelAdmin):
	inlines = [
		UserAdmin,
		AnswerAdmin,
	]

admin.site.register(Vote, VoteAdmin)