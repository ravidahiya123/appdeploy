from django.urls import path
from .views import home, get_download_link, get_stats

urlpatterns = [
    path('', home, name='home'),
    path('get-download-link/', get_download_link, name='get_download_link'),
    path('get-stats/', get_stats, name='get_stats'),

]