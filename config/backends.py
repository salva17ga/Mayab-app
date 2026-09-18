from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

### custom backends coded for this app. 

class EmailBackend(BaseBackend):

    '''
    This class is a custom authentication backend, enabling login for admin site users
    with email instead of username. 
    '''

    def authenticate(self, request, username=None, password=None, **kwargs):

        User = get_user_model()

        email = kwargs.get("email") or username

        if not email or not password:
            return None

        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):

        User = get_user_model()

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None