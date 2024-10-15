from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIToken

class StaticTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return None  # Pas de header Authorization

        if not auth_header.startswith('Bearer '):
            raise AuthenticationFailed('Le token doit commencer par "Bearer"')

        token = auth_header.split(' ')[1]  # Extraire le token après 'Bearer'

        try:
            APIToken.objects.get(token=token)
        except APIToken.DoesNotExist:
            raise AuthenticationFailed('Token invalide ou manquant')

        return (None, None)  # Autorise la requête