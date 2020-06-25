
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('musician/<int:musician_id>/', views.detail, name='detail')
]
