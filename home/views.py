from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from home.models import Setting, ContactForm, ContactMessage
from product.models import *


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:4]  # first 4 product
    products_latest = Product.objects.all().order_by('-id')[:4]  # first 4 product
    products_picked = Product.objects.all().order_by('?')[:4]  # first 4 product
    page = 'home'
    context = {'setting': setting,
               "page": page,
               'products_slider': products_slider,
               'products_latest': products_latest,
               'products_picked': products_picked,
               'category': category}
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent.")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context = {'setting': setting, 'form': form}
    return render(request, 'contact.html', context)


def category_product(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {'products': products,
               'category': category,
               # 'catdata': catdata,
               }
    return render(request, 'category_products.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {'product': product,
               'category': category,
               'images': images,
               'comments': comments,
               }
    return render(request, 'product_detail.html', context)


