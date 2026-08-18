from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import Optional
from books.models import Livro
from decouple import config
from django.db.models import Q

client = genai.Client(
    api_key=config("GEMINI_API_KEY")
)

class BuscaLivros(BaseModel):
    busca: Optional[str] = None
    categoria: Optional[str] = None
    autor: Optional[str] = None
    preco_max: Optional[float] = None
    preco_min: Optional[float] = None
    somente_estoque: bool = False

def interpretar_pergunta(mensagem):

    prompt = f"""
Você é um sistema de interpretação de perguntas para uma
livraria.

Sua única função é identificar os filtros necessários para
pesquisar livros no catálogo.

Pergunta do cliente:
{mensagem}

Extraia somente informações que estejam claramente presentes
na pergunta.

Regras:

- "busca" deve conter palavras relevantes para procurar
  no título, descrição, autor ou categoria.
- "categoria" deve ser preenchida quando o cliente indicar
  um gênero ou categoria.
- "autor" deve ser preenchido quando o cliente mencionar
  um autor.
- "preco_max" deve ser preenchido quando houver um preço máximo.
- "preco_min" deve ser preenchido quando houver um preço mínimo.
- "somente_estoque" deve ser true quando o cliente pedir
  livros disponíveis, em estoque ou que possam ser comprados.
- Se o cliente não mencionar estoque, não presuma que ele
  está procurando somente livros em estoque.
- Não invente informações.
- Não escreva uma resposta para o cliente.
- Retorne somente os filtros.

Exemplos:

Pergunta:
"Quero livros de fantasia por menos de R$ 50"

Resultado:
categoria = "fantasia"
preco_max = 50
somente_estoque = false

Pergunta:
"Vocês têm livros do Machado de Assis?"

Resultado:
autor = "Machado de Assis"
somente_estoque = true

Pergunta:
"Quero O Hobbit"

Resultado:
busca = "O Hobbit"

Pergunta:
"Quero um livro disponível de ficção científica"

Resultado:
categoria = "ficção científica"
somente_estoque = true
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=BuscaLivros,
        ),
    )

    return BuscaLivros.model_validate_json(response.text)

def buscar_livros(filtros):

    queryset = (
        Livro.objects
        .select_related("categoria", "editora")
        .prefetch_related("autores")
        .all()
    )

    if filtros.categoria:
        queryset = queryset.filter(
            categoria__nome__icontains=filtros.categoria
        )

    if filtros.autor:
        queryset = queryset.filter(
            autores__nome__icontains=filtros.autor
        )

    if filtros.preco_max is not None:
        queryset = queryset.filter(
            preco__lte=filtros.preco_max
        )

    if filtros.preco_min is not None:
        queryset = queryset.filter(
            preco__gte=filtros.preco_min
        )

    if filtros.somente_estoque:
        queryset = queryset.filter(
            estoque__gt=0
        )

    if filtros.busca:
        queryset = queryset.filter(
            Q(titulo__icontains=filtros.busca)
            | Q(descricao__icontains=filtros.busca)
            | Q(autores__nome__icontains=filtros.busca)
            | Q(categoria__nome__icontains=filtros.busca)
        )

    return queryset.distinct()