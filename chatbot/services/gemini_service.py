from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import Optional
from books.models import Livro

client = genai.Client()


class BuscaLivros(BaseModel):
    busca: Optional[str] = None
    categoria: Optional[str] = None
    autor: Optional[str] = None
    preco_max: Optional[float] = None
    preco_min: Optional[float] = None
    somente_estoque: bool = False

def interpretar_pergunta(mensagem):
    prompt = f"""
Você é um sistema que interpreta perguntas de clientes
de uma livraria.

Analise a pergunta abaixo e extraia somente os filtros
necessários para pesquisar no catálogo.

Pergunta do cliente:
{mensagem}

Regras:

- "busca" deve conter palavras relevantes para título,
  descrição ou outros campos gerais.
- "categoria" deve ser preenchida quando o cliente indicar
  um gênero ou categoria de livro.
- "autor" deve ser preenchido quando o cliente mencionar
  um autor.
- "preco_max" deve ser preenchido quando houver um preço
  máximo.
- "preco_min" deve ser preenchido quando houver um preço
  mínimo.
- "somente_estoque" deve ser true quando o cliente estiver
  procurando livros disponíveis.
- Não invente informações.
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
            titulo__icontains=filtros.busca
        )

    return queryset.distinct()

def gerar_resposta(mensagem, livros):

    catalogo = []

    for livro in livros:

        autores = ", ".join(
            autor.nome
            for autor in livro.autores.all()
        )

        catalogo.append({
            "titulo": livro.titulo,
            "autores": autores,
            "categoria": livro.categoria.nome,
            "preco": str(livro.preco),
            "estoque": livro.estoque,
            "descricao": livro.descricao,
        })

    prompt = f"""
Você é o assistente virtual de uma livraria.

Responda à pergunta do cliente utilizando SOMENTE
as informações presentes no catálogo abaixo.

Nunca invente livros, autores, preços ou estoque.

Pergunta:
{mensagem}

Catálogo encontrado:
{catalogo}

Responda em português brasileiro, de forma natural,
cordial e objetiva.

Se nenhum livro foi encontrado, informe isso ao cliente
sem inventar alternativas.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text