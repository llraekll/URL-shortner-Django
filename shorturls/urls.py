from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:pk>', views.reroute, name='final')
    # path('url',views.shorturl, name='shorturls')
]
