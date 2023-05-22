from django.shortcuts import render
from django.http import HttpResponse
from . models import Products, Item
from .forms import CreateNewItem

# Create your views here.

def index(response, name):
    ls = Products.objects.get(name=name)
    return render(response, "main/list.html",{"ls":ls})


def home(response):
    return render(response, "main/home.html",{})


def create(response):
    form = CreateNewItem()
    return render(response, "main/create.html",{"form":form})