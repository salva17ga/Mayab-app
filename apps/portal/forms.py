### login form 
from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm


class EmailAdminAuthenticationForm(AdminAuthenticationForm):
    '''
    Since the custom login auth backend works with email field, 
    this class customices the login html form of admin to ask 
    the user for an email 
    '''

    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "autofocus": True,
            }
        ),
    )