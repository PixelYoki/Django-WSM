from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages

# Create your views here.
def index(request):
    form = OrderForm()
    orders = Order.objects.all()
    orders_count = orders.count()
    products = Product.objects.all()
    products_count = products.count()
    workers = User.objects.all()
    workers_count = workers.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {'form': form,
               'orders': orders,
               'products': products,
               'workers_count': workers_count,
               'orders_count': orders_count,
               'products_count': products_count,
               }
    return render(request, 'dashboard/index.html', context)


@login_required()
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders = Order.objects.all()
    orders_count = orders.count()

    items = Product.objects.all()
    products_count = items.count()

    context = {'workers': workers,
               'workers_count': workers_count,
               'orders_count': orders_count,
               'products_count': products_count,
               }
    return render(request, 'dashboard/staff.html', context)


@login_required()
def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    context = {'worker': worker}
    return render(request, 'dashboard/staff_detail.html', context)


@login_required()
def product_list(request):
    form = ProductForm()
    workers = User.objects.all()
    workers_count = workers.count()

    orders = Order.objects.all()
    orders_count = orders.count()

    items = Product.objects.all()
    products_count=items.count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'你已创建{product_name}')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
        context = {'form': form,
                   'items': items,
                   'workers_count': workers_count,
                   'orders_count': orders_count,
                   'products_count':products_count,
                  }
    return render(request, 'dashboard/product.html', context)

@login_required()
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        messages.success(request, f'你删除了{item.name}')
        item.delete()
        return redirect('dashboard-product')

    return render(request, 'dashboard/product_delete.html', {'item': item})

@login_required()
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'你更新了{product_name}')
        return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {'form': form}
    return render(request, 'dashboard/product_update.html', context)


@login_required(login_url='user-login')
def order_list(request):
    orders = Order.objects.all()
    orders_count = orders.count()

    workers = User.objects.all()
    workers_count = workers.count()
    items = Product.objects.all()
    products_count = items.count()
    context = {
        'orders': orders,
        'workers_count': workers_count,
        'orders_count':orders_count,
        'products_count': products_count,
    }
    return render(request, 'dashboard/order.html', context)