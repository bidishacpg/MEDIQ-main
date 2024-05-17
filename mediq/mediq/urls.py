"""
URL configuration for mediq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from mediq import views
from django.conf import settings
from django.conf.urls.static import static

<<<<<<< HEAD

=======
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('book/',views.book, name="book")

]
>>>>>>> 0ee13d0627cb5f07a91306d0d790027f70f4e887

<<<<<<< HEAD

=======
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('doclogin/', views.doclogin, name="login"),
    path('docreg/',views.docreg, name="docregister"),
    path('patreg/',views.patreg, name="patreg")
<<<<<<< HEAD
]
=======
>>>>>>> 4cd2ae36c7fefb81c73acdd43f7aab78ddf5a894
]
>>>>>>> e7cc38101d743837789281a35540a985e617608e
>>>>>>> 0ee13d0627cb5f07a91306d0d790027f70f4e887
