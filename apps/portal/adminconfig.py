from django.contrib.admin.apps import AdminConfig


class PortalAdminConfig(AdminConfig): 
    default_site = 'config.admin.MayabAdminSite'