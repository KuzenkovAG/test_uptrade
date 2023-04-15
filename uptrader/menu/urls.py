from django.urls import path

from . import views


app_name = 'menu'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:menu_slug>/', views.MenuView.as_view(), name='menu_name')
]
