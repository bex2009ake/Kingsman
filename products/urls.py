from django.urls import path
from products.views import *

urlpatterns = [
    path('product/', ProductCreateList.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('order/', ListOrder.as_view(), name='order-list'),
    path('order/<int:pk>/', CreatetOrder.as_view(), name='order-create'),
]