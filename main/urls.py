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
    path("create/" , views.create , name="create"),
]