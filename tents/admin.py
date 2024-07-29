from django.contrib import admin
from .models import Tent

class TentAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'rate')
    search_fields = ('name',)

admin.site.register(Tent, TentAdmin)
