from django.shortcuts import render,redirect
from .models import *
from orders.models import *
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Sum


# Create your views here.

#homepage
def home(request):
    order_object = Orders.objects.all()
    total_amount = Orders.objects.aggregate(Sum('total_amount'))['total_amount__sum']
    context={'datas':order_object,'total_amount':total_amount}
    return render(request,'home.html',context)

# products in store
def manage_product(request):
    product_object=Products.objects.all()
    return render(request,'products.html',{'items':product_object})

# adding items to product table
def add_product(request):
    if request.method=='POST':
        product_name=request.POST['product_name']
        uom=request.POST["unit"]
        price=request.POST["price"]
        available=request.POST["available"]
        queryset=Products.objects.all()
        product_names = queryset.values_list('product_name', flat=True)
        if product_name.title() not in product_names:
            Products.objects.create(product_name=product_name.title(), uom=uom,available_items=available,price=price)
            messages.success(request,'Added succesfully')
            return redirect('manage_product')
        else:
            messages.warning(request,'product already exists')
            return redirect('manage_product')




# update the product table
def get_row_data(request,id):
    if request.method == 'GET':
        row = Products.objects.get(product_id=id)
        data = {
            'id': row.product_id,
            'product_name': row.product_name,
            'unit':row.uom,
            'price':row.price,
            'available_items':row.available_items
        }
        return JsonResponse(data)
    else:
        return HttpResponseBadRequest()


def update_view(request):
    if request.method=='POST':
        product_id=request.POST['id']
        product_name=request.POST['product_name']
        uom=request.POST["unit"]
        price=request.POST["price"]
        available_quantity=request.POST["available_count"]
        update_product=Products.objects.get(product_id=product_id)
        update_product.product_name=product_name
        update_product.uom=uom
        update_product.available_items=int(available_quantity)
        update_product.prices=price
        update_product.save()
    return redirect('manage_product')


def delete_product(request,id):
    delete_product=Products.objects.get(product_id=id)
    delete_product.to_sale='NO'
    delete_product.save()
    messages.info(request,'Deleted sucessfully')
    return redirect('manage_product')
