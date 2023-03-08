from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import NewProductForm
from .models import Product

def detail(request, id):
  product = Product.objects.get(pk=id)

  return render(request, 'product/detail.html', {
    'product': product
  })

# Create your views here.
@login_required
def new(request):
  if request.method == 'POST':
    form = NewProductForm(request.POST, request.FILES)

    if form.is_valid():
      item = form.save(commit=False)
      item.created_by = request.user
      item.save()

      return redirect('home')
  else:
    form = NewProductForm()

  return render(request, 'product/form.html', {
    'form': form,
    'title': 'Novo produto'
  })