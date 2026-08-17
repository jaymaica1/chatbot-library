import django_filters

from .models import Livro


class LivroFilter(django_filters.FilterSet):

    preco_max = django_filters.NumberFilter(
        field_name="preco",
        lookup_expr="lte"
    )

    preco_min = django_filters.NumberFilter(
        field_name="preco",
        lookup_expr="gte"
    )

    em_estoque = django_filters.BooleanFilter(
        method="filtrar_estoque"
    )

    def filtrar_estoque(self, queryset, name, value):
        if value:
            return queryset.filter(estoque__gt=0)

        return queryset

    class Meta:
        model = Livro
        fields = [
            "categoria",
            "editora",
            "preco_min",
            "preco_max",
            "em_estoque",
        ]