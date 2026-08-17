from rest_framework import serializers

from .models import Livro


class LivroSerializer(serializers.ModelSerializer):
    autores = serializers.StringRelatedField(many=True)
    categoria = serializers.StringRelatedField()
    editora = serializers.StringRelatedField()

    class Meta:
        model = Livro
        fields = [
            "id",
            "titulo",
            "isbn",
            "descricao",
            "preco",
            "estoque",
            "ano_publicacao",
            "autores",
            "categoria",
            "editora",
        ]