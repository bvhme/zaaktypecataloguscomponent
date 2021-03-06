from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from ..models import ResultaatType, ZaakInformatieobjectTypeArchiefregime
from .mixins import FilterSearchOrderingAdminMixin, GeldigheidAdminMixin


class ZaakInformatieobjectTypeArchiefregimeInline(admin.TabularInline):
    model = ZaakInformatieobjectTypeArchiefregime
    extra = 1


@admin.register(ResultaatType)
class ResultaatTypeAdmin(GeldigheidAdminMixin, FilterSearchOrderingAdminMixin, admin.ModelAdmin):
    model = ResultaatType

    # List
    list_display = ('resultaattypeomschrijving', 'selectielijstklasse')

    # Details
    fieldsets = (
        (_('Algemeen'), {
            'fields': (
                'resultaattypeomschrijving',
                'resultaattypeomschrijving_generiek',
                'selectielijstklasse',
                'archiefnominatie',
                'archiefactietermijn',
                'brondatum_archiefprocedure',
                'toelichting',
                'heeft_voor_brondatum_archiefprocedure_relevante',
                'is_relevant_voor'
            )
        }),
        (_('Relaties'), {
            'fields': (
                'heeft_verplichte_zot',
                'heeft_verplichte_ziot'
            )
        }),
    )
    filter_horizontal = (
        'heeft_verplichte_zot',
        'heeft_verplichte_ziot',
    )
    raw_id_fields = ('heeft_voor_brondatum_archiefprocedure_relevante', 'is_relevant_voor', )
    inlines = (ZaakInformatieobjectTypeArchiefregimeInline,)  # 'bepaalt_afwijkend_archiefregime_van',
