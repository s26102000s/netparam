from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from .models import course, team, service, product, client,Contact
from .resources import ClientResource

class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource

admin.site.register(course)
admin.site.register(Contact)
admin.site.register(team)
admin.site.register(service)
admin.site.register(product)
admin.site.register(client)
