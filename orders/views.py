from django.shortcuts import render,redirect
from base.models import *
from .models import *
from django.db.models import Sum
from django.contrib import messages


def new_order(request):
    if request.method=='POST':
        name=request.POST['name']
        number=request.POST['number']
        customer_numbers=Orders.objects.all().values_list('mobile_number', flat=True)
        customer_numbers=list(customer_numbers)
        if number not in customer_numbers:
            products=Products.objects.all()
            Orders.objects.create(customer_name=name.title(),mobile_number=number)
            order=Orders.objects.get(mobile_number=number)
            context={'products':products,'order':order}
            return render(request,'order.html',context)
        else:
            messages.warning(request,'Enter valid mobile number')
            return redirect('home')
    
def orders(request):
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['product_name']
        qty=request.POST['quantity']
        total_amount=request.POST['total']
        products=Products.objects.all()
        selected_product=Products.objects.get(product_name=name)
        if int(qty)<=selected_product.available_items:
            selected_product.available_items=selected_product.available_items-int(qty)
            selected_product.save()
            order=Orders.objects.get(order_id=id)
            OrderDetails.objects.create(order_id=order,product_id=selected_product,quantity=qty,total_price=total_amount).save()
            orders=OrderDetails.objects.filter(order_id=id)
            order_items_sum = OrderDetails.objects.filter(order_id=id).aggregate(Sum('total_price'))['total_price__sum']
            order.total_amount=order_items_sum
            order.save()
            # print(order_items_sum)
            # print(orders)
            # for i in orders:
            #     print(i.order_id.order_id,i.product_id.product_id)
            context={'products':products,'order':order,'orders':orders,'order_items_sum':order_items_sum}
            return render(request,'order.html',context)
        else:
            messages.warning(request,'Entered quantity is unavailable')
            return redirect('orders')