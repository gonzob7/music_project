
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('musician/<int:musician_id>/', views.detail, name='detail'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
]
