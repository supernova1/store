from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, render

from .models import Basket, Product, ProductCategory


def index(request):
    return render(request, "products/index.html", {"title": "Store"})


def products(request, category_id=None, page=1):
    context = {
        "title": "Store - Каталог",
        "categories": ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page)
    context.update({"products": products_paginator})

    return render(request, "products/products.html", context=context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(pk=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(pk=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
