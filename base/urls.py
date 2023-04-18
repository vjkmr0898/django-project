from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('manage_product',views.manage_product,name='manage_product'),
    path('add_product',views.add_product,name='add_product'),
    path('get_row_data/<int:id>/',views.get_row_data,name='get_row_data'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('update_view',views.update_view,name='update_view')
]