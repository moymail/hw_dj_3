from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting = request.GET.get('sort')

    def sort_phone(param):
        phones = Phone.objects.all().order_by(param)
        context = {'phones': phones}
        return render(request, 'catalog.html', context)
    if sorting == 'name':
        return sort_phone('name')
    elif sorting == 'min_price':
        return sort_phone('price')
    elif sorting == 'max_price':
        return sort_phone('-price')
    else:
        return sort_phone('id')


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
