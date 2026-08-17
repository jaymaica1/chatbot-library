from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from .filters import LivroFilter
from .models import Livro
from .serializers import LivroSerializer


class LivroListView(generics.ListAPIView):

    queryset = (
        Livro.objects
        .select_related("categoria", "editora")
        .prefetch_related("autores")
        .all()
    )

    serializer_class = LivroSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_class = LivroFilter

    search_fields = [
        "titulo",
        "isbn",
        "descricao",
        "autores__nome",
        "categoria__nome",
        "editora__nome",
    ]

class LivroDetailView(generics.RetrieveAPIView):

    queryset = (
        Livro.objects
        .select_related("categoria", "editora")
        .prefetch_related("autores")
        .all()
    )

    serializer_class = LivroSerializer