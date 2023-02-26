from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    phones = Phone.objects.all()
    info = request.GET.get('sort')
    print(info)
    print(type(info))
    if info == 'name':
        phones = Phone.objects.order_by('name')
    if info == 'min_price':
        phones = Phone.objects.order_by('price')
    if info == 'max_price':
        phones = Phone.objects.order_by('price')[::-1]
    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    phones = Phone.objects.filter(slug=slug)
    template = 'product.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)
