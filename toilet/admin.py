from django.contrib import admin
from .models import Toilet


class ToiletAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'level')
    list_display_links = ('id', 'place', 'level')


admin.site.register(Toilet, ToiletAdmin)
