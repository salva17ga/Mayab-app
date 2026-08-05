from django.contrib import admin

# subclassing adminsite 

class MayabAdminSite(admin.AdminSite): 
    site_title= 'Mayab Admin'
    site_header = 'Sistema Mayab'
    index_title = 'Administración del sistema'
