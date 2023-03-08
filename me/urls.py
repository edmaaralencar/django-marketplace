from django.urls import path

from . import views

app_name = 'me'

urlpatterns = [
  path('products/', views.products, name="products"),
  path('chats/', views.chats, name="chats"),
]