"""
URL configuration for mayab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
import apps.portal.views
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apps.portal.views.index, name = 'index'), 
    path('about', apps.portal.views.about, name = 'about'), 
    path('furnitures', apps.portal.views.furnitures, name = 'furnitures'), 
    path('art', apps.portal.views.art, name = 'art'), 
    path('decoration', apps.portal.views.decoration, name = 'decoration'), 
    path('exhibitions', apps.portal.views.exhibitions, name = 'exhibitions'), 
    path('interior_design', apps.portal.views.interior_design, name = 'interior_design'), 
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            email_template_name="registration/password_reset_email.html",
            subject_template_name="registration/password_reset_subject.txt",
        ),
        name="admin_password_reset",
    ),

    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html",
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

