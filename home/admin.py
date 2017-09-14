from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Email


class EmailAdmin(ImportExportModelAdmin):
    readonly_fields = ('enter_date',)
    list_display = ('email', 'enter_date')


admin.site.register(Email, EmailAdmin)


class EmailResource(resources.ModelResource):
    class Meta:
        model = Email
        exclude = ('id',)
