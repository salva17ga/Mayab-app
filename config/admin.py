from django.contrib import admin
from apps.portal.forms import EmailAdminAuthenticationForm
# subclassing adminsite 

class MayabAdminSite(admin.AdminSite): 
    site_title= 'Mayab Admin'
    site_header = 'Sistema Mayab'
    index_title = 'Administración del sistema'
    login_form = EmailAdminAuthenticationForm


