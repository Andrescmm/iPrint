from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Products, Item
from .forms import CreateNewItem

# Create your views here.

def index(response, id):
    ls = Products.objects.get(id=id)
   
    if response.method == "POST":
       print(response.POST)
       if response.POST.get("save"):
          for item in ls.item_set.all():
             if response.POST.get("c"+str(item.id)) == "clicked":
                item.complete = True
             else:
                item.complete = False
             item.save()       
       
       elif response.POST.get("newItem"):
          txt = response.POST.get("new")

          if len(txt) > 2:
             ls.item_set.create(text=txt, complete=False)
          else:
             print ("invalid")
    

    return render(response, "main/list.html",{"ls":ls})


def home(response):
    return render(response, "main/home.html",{})

def welcome(response):
    return render(response, "main/welcome.html",{})

def about(response):
    return render(response, "main/about.html",{})


def services(response):
    return render(response, "main/services.html",{})

def prices(response):
    return render(response, "main/prices.html",{})

def contact(response):
    return render(response, "main/contact.html",{})

def shop(response):
    return render(response, "main/shop.html",{})

def shop_single(response):
    return render(response, "main/shop-single.html",{})

def cart(response):
    return render(response, "main/cart.html",{})

def checkout(response):
    return render(response, "main/checkout.html",{})

def login(response):
    return render(response, "main/login.html",{})

def user(response):
    return render(response, "main/user.html",{})

def detail1(response):
    return render(response, "main/portfolio-details.html",{})
def detail2(response):
    return render(response, "main/portfolio-details2.html",{})
def detail3(response):
    return render(response, "main/portfolio-details3.html",{})


def create(response):
    if response.method == "POST":
      form = CreateNewItem(response.POST)

      if form.is_valid():
        n = form.cleaned_data["name"]
        t = Products(name=n)
        t.save()
          
      return HttpResponseRedirect("/%i" %t.id)  
       
    else:
       form = CreateNewItem()
    return render(response, "main/create.html",{"form":form})