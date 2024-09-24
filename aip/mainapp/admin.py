from typing import Sequence
from django.contrib import admin
from django.http import HttpRequest
from .models import Attraction

admin.site.site_header = "Сочи Парк"
admin.site.site_title = "Аттракционы Сочи Парка"
admin.site.index_title = "Сочи Парк"


class AttractionAdmin(admin.ModelAdmin):
    list_display = ("name", "height", "age", "active", "order")
    list_editable = ("active", "order")
    list_filter = ("active", )
    ordering = ("order", "name")
    show_facets = admin.ShowFacets.ALWAYS #adding counter on active/not active attractions filter

    #removing bulk actions on the multiple Attractions
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ProxyAttraction(Attraction):
    class Meta:
        verbose_name = "Активность"
        verbose_name_plural = "Аттракционы в работе"
        proxy = True

        
class MinorAttractionAdmin(admin.ModelAdmin):
    list_display = ("name", "active",)
    list_editable = ("active",)
    list_filter = ("active", )
    ordering = ("order", "name")
    show_facets = admin.ShowFacets.ALWAYS #adding counter on active/not active attractions filter

    #Removing possibility to change every Attraction on a DetailedView
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return None

    #removing bulk actions on the multiple Attractions
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


#registering models
admin.site.register(Attraction, AttractionAdmin)
admin.site.register(ProxyAttraction, MinorAttractionAdmin)