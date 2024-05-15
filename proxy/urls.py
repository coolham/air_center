from django.urls import path
from . import views

urlpatterns = [
    path('proxies/', views.ProxyListView.as_view()),
    path('proxies/<int:pk>/', views.ProxyDetailView.as_view()),
]