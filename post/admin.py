from django.contrib import admin

# Register your models here.
#引入包
from .models import *
#注册models到后台
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','created')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostModelAdmin)


