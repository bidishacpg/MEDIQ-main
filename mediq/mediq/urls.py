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
    path('services/',views.services, name="services"),
<<<<<<< HEAD
    path('doclogin/', views.doclogin, name="doclogin"),
    path('docreg/',views.docreg, name="docreg"),
    path('patreg/',views.patreg, name="patreg"),
    path('book/',views.book, name="book"),
    path('hospreg/',views.hospreg, name="hospreg"),
    path('doclist/',views.doclist, name="doclist"),
    path('hosdetail/',views.hosdetail, name="hosdetail"),
    path('about/',views.about, name="about"),
    path('services/',views.services,name="services")
=======
    path('doclist/',views.doclist, name="doclist"),
    path('hosdetail/',views.hosdetail, name="hosdetail")
    ]
>>>>>>> d2e85609004767b658755b5f398655d71eeb6b83

if settings.DEBUG:
<<<<<<< HEAD
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> d2e85609004767b658755b5f398655d71eeb6b83
