from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
  path('<int:id>/', views.detail, name="detail"),
  path('new/', views.new, name="new"),
]