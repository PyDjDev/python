from django.contrib import admin

# Register your models here.
from blogbase.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
	fields = (('title', 'pud_date'), 'body')
	date_hierarchy = 'pud_date'	
	readonly_fields = ('pud_date',)

admin.site.register(BlogPost, BlogPostAdmin)