from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from product.models import Product
from .models import Chat, Message

# Create your views here.
@login_required
def detail(request, id):
  buyerUsername = request.GET.get('buyer')

  product = Product.objects.get(pk=id)
  buyer = User.objects.get(username=buyerUsername)
  user = request.user
  creator_of_product = product.created_by

  messages = None
  chat = None

  try:
    chat = Chat.objects.get(product=product, seller=creator_of_product, buyer=buyer)

    messages = Message.objects.filter(chat=chat)
  except ObjectDoesNotExist:
    chat = Chat(buyer=user, seller=product.created_by, product=product)
    chat.save()


  return render(request, 'chat/index.html', {
    'product': product,
    'chat': chat,
    'messages': messages
  })
