from rest_flex_fields.views import FlexFieldsMixin
from rest_framework import viewsets

from ...datamodel.models import BesluitType
from ..serializers import BesluitTypeSerializer
from ..utils.viewsets import (
    FilterSearchOrderingViewSetMixin, NestedViewSetMixin
)


class BesluitTypeViewSet(NestedViewSetMixin, FilterSearchOrderingViewSetMixin, FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Generieke aanduiding van de aard van een besluit.

    list:
    Alle BESLUITTYPEn van de besluiten die het resultaat kunnen zijn van het zaakgericht werken van de behandelende
    organisatie(s).
    """
    queryset = BesluitType.objects.all()
    serializer_class = BesluitTypeSerializer
