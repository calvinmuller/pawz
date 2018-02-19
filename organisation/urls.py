from django.urls import path

from . import views

app_name = 'organisation'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug>/', views.DetailView.as_view(), name='detail')
]