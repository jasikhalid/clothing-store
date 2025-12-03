"""clan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clan_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('reg',views.regis),
    path('log',views.logi),
    path('logout',views.logout),
    path('shop',views.shop),
    path('shopcart',views.shop_cart),
    path('product-details',views.product_details),
    path('contact',views.contact),
    path('checkout',views.checkout),
    # path('adminpanel',views.adminpanel),
    path('admin-pro',views.admin_pro),
    path('product',views.product),
    path('update',views.update),
    path('delete',views.delete),
    path('dashboard',views.dashboard),
    path('orders', views.admin_orders, name='admin_orders'),
    path('message',views.message),
    path('blog',views.blog),
    path('blog-details',views.blog_details),
    path('favorite',views.favorite),
    path('add_to_wishlist/<str:ids>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<str:ids>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add_to_cart/<str:ids>/', views.add_to_cart, name='add_to_cart'),
    path('inc/<str:ids>/', views.inc, name='inc'),
    path('dec/<str:ids>/', views.dec, name='dec'),
    path('men',views.men),
    path('women',views.women),
    path('payment',views.payment),
    path('luxury',views.luxury),
    path('street',views.street),
    path('sport',views.sport),
    path('footwear',views.footwear),
    path('accessory',views.accessory),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
