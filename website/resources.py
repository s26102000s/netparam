from import_export import resources
from .models import client

class ClientResource(resources.ModelResource):
    class Meta:
        model = client
        fields = ('__all__')
