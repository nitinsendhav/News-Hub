# admin pass. News@1234 
from django.contrib import admin
from .models import Category, News, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    

admin.site.register(Category, CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['cate','title', 'image', 'desc', 'publish']

admin.site.register(News, NewsAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email","content"]
    
admin.site.register(Comment,CommentAdmin)