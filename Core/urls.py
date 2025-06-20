"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static  # Add this import
from django.urls import path
from home.views import *
from vege.views import *
urlpatterns = [
    path('',home,name="home"),
    path('admin/', admin.site.urls),  # Add this line
    path('recipies/',recipies,name="recipies"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('logout/',logout_page,name='logout_page'),
    path('login/', login_page, name='login'),
    path('register/',register,name="register"),
    path('update_receipe/<int:id>',update_receipe,name=""),
    path('delete_recipie/<int:id>',delete_recipie,name="")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)