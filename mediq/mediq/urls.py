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







urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('doclogin/', views.doclogin, name="login"),
    path('docreg/',views.docreg, name="docreg"),
    path('patreg/',views.patreg, name="patreg"),
    path('book/',views.book, name="book"),
    path('hospregister/',views.hospreg, name="hospregister"),
<<<<<<< HEAD
    path('hosdetails/',views.hosdetails, name="hosdetails"),
    path('contact/',views.contact, name="contact"),
    path('aboutus/',views.aboutus, name="aboutus")
    
=======
    path('services/',views.services, name="services"),
    path('doclogin/', views.doclogin, name="doclogin"),
    path('docreg/',views.docreg, name="docreg"),
    path('patreg/',views.patreg, name="patreg"),
    path('book/',views.book, name="book"),
    path('hospreg/',views.hospreg, name="hospreg"),
    path('doclist/',views.doclist, name="doclist"),
    path('hosdetail/',views.hosdetail, name="hosdetail"),
    path('about/',views.about, name="about"),
    path('services/',views.services,name="services")
>>>>>>> 757396d0c3b1c1172a56bfbfdc9039e924e6b05b
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

