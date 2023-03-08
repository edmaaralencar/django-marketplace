from django.shortcuts import render
from django.db.models import Q

from product.models import Product
from chat.models import Chat

# Create your views here.
def products(request):
  products = Product.objects.filter(created_by=request.user)

  return render(request, 'me/products.html', {
    'products': products
  })

def chats(request):
  chats = Chat.objects.filter(Q(buyer=request.user) | Q(seller=request.user))

  return render(request, 'me/chats.html', {
    'chats': chats
  })