from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product


def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'catalog/category_detail.html', context)


@api_view(['GET'])
def api_product_list(request):
    category_slug = request.GET.get('category')

    products = Product.objects.filter(available=True)
    if category_slug:
        products = products.filter(category__slug=category_slug)

    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'slug': product.slug,
            'description': product.description,
            'price': str(product.price),
            'category': product.category.name,
            'stock': product.stock,
            'image': product.image.url if product.image else None,
        })

    return Response(data)


@api_view(['GET'])
def api_product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)

    data = {
        'id': product.id,
        'name': product.name,
        'slug': product.slug,
        'description': product.description,
        'price': str(product.price),
        'category': product.category.name,
        'stock': product.stock,
        'image': product.image.url if product.image else None,
    }

    return Response(data)
