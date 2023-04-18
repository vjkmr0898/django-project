from django.urls import path,include
from . import views


urlpatterns = [
path('new_order',views.new_order,name='new_order'),
path('orders',views.orders,name='orders'),
]
