from django.contrib import admin

from .models import Autor, Categoria, Editora, Livro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "categoria",
        "editora",
        "preco",
        "estoque",
    )

    search_fields = (
        "titulo",
        "isbn",
        "autores__nome",
    )

    list_filter = (
        "categoria",
        "editora",
    )
