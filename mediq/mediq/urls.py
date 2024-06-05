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
    path('doclogin/', views.doclogin, name="doclogin"),
    path('docreg/',views.docreg, name="docreg"),
    path('hosplogin/',views.hosplogin, name="hosplogin"),
    path('patreg/',views.patreg, name="patreg"),
    path('patlogin/',views.patlogin, name="patlogin"),
    path('book/',views.book, name="book"),
    path('hospregister/',views.hospreg, name="hospregister"),
    path('contact/',views.contact, name="contact"),
    path('aboutus/',views.aboutus, name="aboutus"),
    path('services/',views.services,name="services"),
    path('doclist/',views.doclist,name="doclist"),
    path('hosplist/',views.hosplist,name="hosplist"),
    path('ambulance/',views.ambulance,name="ambulance"),
    path('pathome/',views.pathome,name="pathome"),
    path('dochome/',views.dochome,name="dochome"),
    path('hosphome/',views.hosphome,name="hosphome"),
    path('doctorprofile/<id>',views.doctorprofile,name="doctorprofile"),
     path('hosplogout/', views.hosplogout, name='hosplogout'),
     path('patlogout/', views.patlogout, name='patlogout'),
     path('doclogout/', views.doclogout, name='doclogout'),
     path('hospage/<id>',views.hospage,name="hospage")


    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

