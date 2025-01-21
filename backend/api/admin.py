from django.contrib import admin
from .models import *
class NewsAdmin(admin.ModelAdmin):
    list_display = ("Title","news_date","category")
    list_filter = ("category",)
    list_per_page = 4
    search_fields = ("Title",)


# Register your models here.
admin.site.register(Category)
admin.site.register(News,NewsAdmin)
