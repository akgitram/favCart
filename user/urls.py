from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('index/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('services/',views.services),
    path('myorder/',views.myorder),
    path('myprofile/',views.myprofile),
    path('product/',views.prod),
    path('signup/',views.signup),
    path('Signin/',views.Signin),
    path('viewsdetails/',views.viewsdetails),
    path('process/',views.process),
    path('logout/',views.logout),
    path('cart/',views.cart),
    
]