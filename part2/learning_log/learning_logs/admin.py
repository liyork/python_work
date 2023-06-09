from django.contrib import admin

# Register your models here.
from .models import Topic, Entry

# 注册自己的模型
admin.site.register(Topic)
admin.site.register(Entry)
