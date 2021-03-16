"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin                        # default
from django.urls import path,include 

from . import views                    # default
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [                                        # default
    path('admin/', admin.site.urls),                      # default
    path('', include('home.urls')),


    
    path('signin/', views.signin),
    path('postsign/', views.postsign),
    path('logout/',views.logout, name="log"),
    path('signup/', views.signup, name="signup"),
    path('postsignup/', views.postsignup, name="postsignup"),
    path('create/',views.create, name="create"),
    path('post_create/', views.post_create)
]




