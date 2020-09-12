from django.shortcuts import render
from .models import Cat, Cat_Photo
from django.http import Http404

def index(request):
    return render(request, 'main/index.html')

def contacts(request):
    return render(request, 'main/contact.html')

def cats(request):
    cats = Cat.objects.filter(sale = True)
    return render(request, 'main/cats.html', context = {'cats':cats})

def sold_cats(request):
    cats = Cat.objects.all()
    return render(request, 'main/sold_cats.html', context = {'cats':cats})

def cat_detail(request, cat_id):
    try:
        cat = Cat.objects.get(pk = cat_id)
        photos = Cat_Photo.objects.filter(fk_cat = cat_id)
        context = {'cat': cat, 'photos':photos}
    except Cat.DoesNotExist:
        raise Http404('Koт не найден')
    return render(request, 'main/cat_detail.html', context = context)