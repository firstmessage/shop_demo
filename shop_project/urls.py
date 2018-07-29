"""shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# стандартный вью для админки
from django.contrib import admin
#from django.contrib.auth import authenticate, login
# модуль Джанго для определения URL'ов
from django.urls import path 
# импортируем наш файл views из shop_app
from shop_app import views 
from django.conf.urls import include

# говорим Джанго о том, что хотим отображать наш вью на главной странице
# а строчкой ниже, кстати ссылка на нашу админку, про нее позже
urlpatterns = [ 
    #ссылка на логин и так далее LoginView, LogoutView и другие.
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/SignUp', views.SignUpView.as_view(), name='SignUp'),
    #ссылка на форму заказа 
    path('products/<int:pk>/order', views.OrderFormView.as_view(), name='product_order'),
# наш View для конкретного продукта из прошлого урока
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
# добавляем новую строчку в urlpatterns
    path('products/new/', views.ProductCreate.as_view(), name='product_create'), 
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'), 
    path('products/<int:pk>/del/', views.ProductDelete.as_view(), name='product_delete'), 
    path('', views.StartPage.as_view(),name='index'), 
#    path('product/<int:pk>/', views.ProductDetail.as_view(), name='detail'),
     path('category/<int:pk>/', views.CategoryDetail.as_view(), name='CategoryDetail'),
#  path('product/', views.ProductListView.as_view(),name='products'), 
#  path('category/', views.CategoryListView.as_view(),name='category'), 
    path('admin/', admin.site.urls), 
]