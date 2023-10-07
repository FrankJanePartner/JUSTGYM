from django.urls import path

from .views import product_all, product_detail, category_list, about, errorPage, orderComplete, checkout, policy

app_name = 'store'

urlpatterns = [
    path('', product_all, name='product_all'),
    path('item/<slug:slug>', product_detail, name='product_detail'),
    path(
        'shop/<slug:category_slug>/',
        category_list,
        name='category_list'
    ),
    path("about/", about, name="about"),
    path("errorPage/", errorPage, name="errorPage"),
    path("orderComplete/", orderComplete, name="orderComplete"),
    path("checkout/", checkout, name="checkout"),
    path("policy/", policy, name="policy"),
]
 

# from django.urls import path
# from .views import home, shop, about, errorPage, details, orderComplete, checkout, policy

# app_name = 'store'
# urlpatterns = [
#     path("", home, name="home"),
#     path(
#         'shop/<slug:category_slug>/',
#         home,
#         name='home'
#     ),
#     path("shop/", shop, name="shop"),
#     path("about/", about, name="about"),
#     path("details/<slug:slug>", details, name="details"),
#     path("errorPage/", errorPage, name="errorPage"),
#     path("orderComplete/", orderComplete, name="orderComplete"),
#     path("checkout/", checkout, name="checkout"),
#     path("policy/", policy, name="policy"),
# ]
