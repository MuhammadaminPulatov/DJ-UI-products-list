from django.shortcuts import render, get_object_or_404, redirect
from form.models import Product


def main_view(request):
    return render(request, 'form.html')


def add_product_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        count = request.POST.get('count')
        rating = request.POST.get('rating')

        Product.objects.create(
            name=name,
            desc=desc,
            price=price,
            count=count,
            rating=rating
        )
        return redirect('product-list')
    return render(request, 'form.html')


def product_view(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.desc = request.POST.get('desc')
        product.price = request.POST.get('price')
        product.count = request.POST.get('count')
        product.rating = request.POST.get('rating')
        product.save()
        return redirect('product-list')

    return render(request, 'edit.html', {'product': product})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product-list')

    return render(request, 'confirm_delete.html', {'product': product})
