from django.contrib import admin
from .models import Attraction

admin.site.site_header = "Сочи Парк"
admin.site.site_title = "Аттракционы Сочи Парка"
admin.site.index_title = "Сочи Парк"


class AttractionAdmin(admin.ModelAdmin):
    list_display = ("name", "height", "age", "active", "order")
    list_editable = ("active", "order")
    list_filter = ("active", )
    ordering = ("order", "name")
    show_facets = admin.ShowFacets.ALWAYS

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Attraction, AttractionAdmin)

