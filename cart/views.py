from django.shortcuts import render, redirect
from django.contrib import messages

def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    pass

def cart_delete(request):
    pass

def cart_update(request):
    pass