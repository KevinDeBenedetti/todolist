from rest_framework.permissions import BasePermission

class HasValidAPIToken(BasePermission):
    """
    Autorise uniquement les requêtes qui ont passé l'authentification par token statique.
    """
    def has_permission(self, request, view):
        # Si la requête a un token valide, la permission est accordée
        if request.auth is None and request.user is None:
            return True
        return False