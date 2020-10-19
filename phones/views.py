from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort')

    #если есть параметр
    if sort_type:
        if sort_type == 'name':
            #сортируем по имени
            phones = Phone.objects.order_by('name')
        elif sort_type == 'min_price':
            # сортируем от минимальной до максимальной цены
            phones = Phone.objects.order_by('price')
        elif sort_type == 'max_price':
            # сортируем от минимальной до максимальной цены
            phones = Phone.objects.order_by('-price')
        else:
            #стандартный вариант
            phones = Phone.objects.all()
    else:
        # стандартный вариант
        phones = Phone.objects.all()

    #phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    #здесь нам нужен фильтр, чтобы выбрать только нужный нам телефон
    phone = Phone.objects.filter(slug=slug).first()
    #ls=list(phone)

    #context = {'phone': ls[0]}
    context = {'phone': phone}

    #context = {'phone': Phone.objects.filter(slug=slug)}
    return render(request, template, context)
