from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Todo List API",
        default_version='v1',
        description=(
            "L'API de gestion de tâches permet de gérer les tâches quotidiennes, "
            "de les organiser et de les suivre efficacement. Vous pouvez créer, "
            "modifier, supprimer des tâches et suivre leur état de complétion. "
            "L'API est sécurisée via des tokens statiques et permet des accès "
            "publics limités."
        ),
        terms_of_service="https://todolist.kevindb.dev/terms/",
        contact=openapi.Contact(
            name="Kevin De Benedetti",
            email="contact@kevindb.dev",
            url="https://kevindb.dev"
        ),
        license=openapi.License(
            name="MIT License",
            url="https://opensource.org/licenses/MIT"
        ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)