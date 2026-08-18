from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services.gemini_service import (
    interpretar_pergunta,
    buscar_livros,
    gerar_mensagem,
)


class ChatView(APIView):

    def post(self, request):

        mensagem = request.data.get("message")

        if not mensagem:
            return Response(
                {
                    "error": "A mensagem não pode estar vazia."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            # 1. Gemini interpreta a pergunta
            filtros = interpretar_pergunta(mensagem)

            # 2. Django consulta o PostgreSQL
            livros = buscar_livros(filtros)

            # 3. Django prepara os dados para o Angular
            livros_data = [
                {
                    "title": livro.titulo,
                    "author": ", ".join(
                        autor.nome
                        for autor in livro.autores.all()
                    ),
                    "category": livro.categoria.nome,
                    "price": str(livro.preco),
                    "description": livro.descricao,
                }
                for livro in livros
            ]

            # 4. A resposta textual agora é criada pelo Django
            resposta = gerar_mensagem(
                filtros,
                len(livros_data)
            )

            return Response({
                "message": resposta,
                "books": livros_data
            })

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )