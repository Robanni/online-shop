from django.shortcuts import render

def cart_add(request, product_id):
    return render(request,'index.html')

def cart_change(request, product_id):
    return render(request,'index.html')

def cart_remove(request, product_id):
    return render(request,'index.html')