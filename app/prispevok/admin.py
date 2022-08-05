from django.contrib import admin
from .models import Prispevok


class PrispevokAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ("title",)
    search_fields = ['title', 'body']


admin.site.register(Prispevok, PrispevokAdmin)
