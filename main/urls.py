from django.urls import path 

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("init" , views.home , name="home"),
    # path("home" , views.welcome , name="welcome"),
    path("about" , views.about , name="about"),
    path("services" , views.services , name="services"),
    path("prices" , views.prices , name="prices"),
    path("contact" , views.contact , name="contact"),
    path("shop" , views.shop , name="shop"),
    path("shop-single" , views.shop_single , name="shop-single"),
    path("cart" , views.cart , name="cart"),
    path("checkout" , views.checkout , name="checkout"),
    path("" , views.login , name="login"),
    path("user" , views.user , name="user"),
    path("detail1" , views.detail1 , name="detail1"),
    path("detail2" , views.detail2 , name="detail2"),
    path("detail3" , views.detail3 , name="detail3"),
    path("create/" , views.create , name="create"),
    
]