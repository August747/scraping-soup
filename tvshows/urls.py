from django.urls import path
from .views import top_tvshows

urlpatterns = [
    path('tvshows/', top_tvshows, name='tvshows')
]
