from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignupForm

from product.models import Product

# Create your views here.
def home(request):
  products = Product.objects.all()

  return render(request, 'core/home.html', {
    'products': products
  })

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)

    if form.is_valid():
      user = form.save()

      login(request, user)

      return redirect('home')

  return render(request, 'core/signup.html')