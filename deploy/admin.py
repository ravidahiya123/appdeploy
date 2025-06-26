from django.contrib import admin
from .models import AppLink

# Register your models here.

@admin.register(AppLink)
class AppLinkAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'download_link', 'used', 'created_at')
    list_filter = ('used', 'app_name')
    search_fields = ('download_link',)