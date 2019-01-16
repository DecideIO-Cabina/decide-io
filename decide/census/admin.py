from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
from .models import Census
# from core.models import Census
from import_export import resources

class CensusAdmin(admin.ModelAdmin):
    list_display = ('voting_id', 'voter_id')
    list_filter = ('voting_id', )

    search_fields = ('voter_id', )



class CensusResource(resources.ModelResource):
    class Meta:
        model = Census
# admin.site.register(Census, CensusAdmin)

@admin.register(Census)
class ViewAdmin(ImportExportModelAdmin):
    pass