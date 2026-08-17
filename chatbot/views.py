from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services.gemini_service import (
    interpretar_pergunta,
    buscar_livros,
    gerar_resposta,
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

            filtros = interpretar_pergunta(mensagem)

            livros = buscar_livros(filtros)

            resposta = gerar_resposta(
                mensagem,
                livros
            )

            return Response({
                "message": resposta
            })

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )