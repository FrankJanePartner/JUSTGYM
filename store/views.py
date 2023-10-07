from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    return render(request, 'home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'detail.html', {'product': product})

def about(request):
    return render(request, 'about.html')

def errorPage(request):
    return render(request, '404-page.html')

def checkout(request):
    return render(request, 'checkout.html')

def orderComplete(request):
    return render(request, 'order-complete.html')

def policy(request):
    return render(request, 'policy.html')

# def home(request):
#     products = Product.products.all()
#     return render(request, 'home.html')

# def shop(request, category_slug=None):
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=category)
#     context = {
#         'category': category,
#         'products': products
#     }
#     return render(request, 'shop.html', {'products': products})

