"""TODOs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page, name="Welcome" ),
    path('items/',views.items,name="Items"),
    path('signin/',views.signin,name="Create Account"),
    path('login/signin/',views.signin,name="Create Account"),
    path('acc_created/',views.acc_created,name="Account Created"),
    path('login/',views.log_in,name="Log In"),
    path('login/hanglelogin/',views.handlelogin,name="Logged In"),
    path('logout/',views.handlelogout,name="Log Out"),
    path('additem/',views.additem,name="Add Item"),
    path('itemcompleted/',views.complete_item,name="Complete Item"),
    path('itemdeleted/',views.delete_item,name="Deleted Item"),
    path('profile/',views.profile,name="Profile"),
    path('edit_profile/',views.edit_profile,name="Edit Profile"),
]
