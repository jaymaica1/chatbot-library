from decimal import Decimal

from django.core.management.base import BaseCommand

from books.models import Autor, Categoria, Editora, Livro


class Command(BaseCommand):
    help = "Cadastra dados iniciais da livraria"

    def handle(self, *args, **options):

        categorias = {}
        nomes_categorias = [
            "Romance",
            "Fantasia",
            "Literatura Brasileira",
            "Ficção Científica",
            "Filosofia",
            "História",
            "Biografia",
            "Infantojuvenil",
        ]

        for nome in nomes_categorias:
            categoria, _ = Categoria.objects.get_or_create(
                nome=nome
            )
            categorias[nome] = categoria

        autores = {}
        nomes_autores = [
            "Machado de Assis",
            "J. R. R. Tolkien",
            "George Orwell",
            "Jane Austen",
            "Clarice Lispector",
            "Fiódor Dostoiévski",
            "Jorge Amado",
            "Mary Shelley",
            "Antoine de Saint-Exupéry",
            "Gabriel García Márquez",
        ]

        for nome in nomes_autores:
            autor, _ = Autor.objects.get_or_create(
                nome=nome
            )
            autores[nome] = autor

        editoras = {}
        nomes_editoras = [
            "Companhia das Letras",
            "Rocco",
            "Record",
            "Editora 34",
            "Intrínseca",
            "Aleph",
            "Penguin",
        ]

        for nome in nomes_editoras:
            editora, _ = Editora.objects.get_or_create(
                nome=nome
            )
            editoras[nome] = editora

        livros = [
            {
                "titulo": "Dom Casmurro",
                "isbn": "9780000000001",
                "descricao": (
                    "Romance de Machado de Assis narrado por "
                    "Bento Santiago, marcado por memórias, "
                    "ciúmes e dúvidas sobre Capitu."
                ),
                "preco": Decimal("39.90"),
                "estoque": 8,
                "ano": 1899,
                "autores": ["Machado de Assis"],
                "categoria": "Literatura Brasileira",
                "editora": "Companhia das Letras",
            },
            {
                "titulo": "Memórias Póstumas de Brás Cubas",
                "isbn": "9780000000002",
                "descricao": (
                    "Romance de Machado de Assis narrado por "
                    "um personagem que conta sua história depois "
                    "da morte."
                ),
                "preco": Decimal("42.90"),
                "estoque": 5,
                "ano": 1881,
                "autores": ["Machado de Assis"],
                "categoria": "Literatura Brasileira",
                "editora": "Companhia das Letras",
            },
            {
                "titulo": "O Hobbit",
                "isbn": "9780000000003",
                "descricao": (
                    "Aventura de Bilbo Bolseiro em uma jornada "
                    "pela Terra-média ao lado de anões e Gandalf."
                ),
                "preco": Decimal("49.90"),
                "estoque": 12,
                "ano": 1937,
                "autores": ["J. R. R. Tolkien"],
                "categoria": "Fantasia",
                "editora": "Rocco",
            },
            {
                "titulo": "O Senhor dos Anéis",
                "isbn": "9780000000004",
                "descricao": (
                    "Épica aventura de fantasia ambientada na "
                    "Terra-média e centrada na destruição do Um Anel."
                ),
                "preco": Decimal("89.90"),
                "estoque": 7,
                "ano": 1954,
                "autores": ["J. R. R. Tolkien"],
                "categoria": "Fantasia",
                "editora": "Rocco",
            },
            {
                "titulo": "1984",
                "isbn": "9780000000005",
                "descricao": (
                    "Romance distópico sobre uma sociedade "
                    "controlada por vigilância e manipulação."
                ),
                "preco": Decimal("34.90"),
                "estoque": 15,
                "ano": 1949,
                "autores": ["George Orwell"],
                "categoria": "Ficção Científica",
                "editora": "Companhia das Letras",
            },
            {
                "titulo": "A Revolução dos Bichos",
                "isbn": "9780000000006",
                "descricao": (
                    "Fábula política que apresenta animais "
                    "revoltados contra seus donos."
                ),
                "preco": Decimal("29.90"),
                "estoque": 10,
                "ano": 1945,
                "autores": ["George Orwell"],
                "categoria": "Ficção Científica",
                "editora": "Companhia das Letras",
            },
            {
                "titulo": "Orgulho e Preconceito",
                "isbn": "9780000000007",
                "descricao": (
                    "Romance de Jane Austen sobre Elizabeth Bennet "
                    "e suas relações familiares e amorosas."
                ),
                "preco": Decimal("44.90"),
                "estoque": 9,
                "ano": 1813,
                "autores": ["Jane Austen"],
                "categoria": "Romance",
                "editora": "Penguin",
            },
            {
                "titulo": "Razão e Sensibilidade",
                "isbn": "9780000000008",
                "descricao": (
                    "Romance que acompanha as irmãs Elinor e "
                    "Marianne e suas diferentes formas de lidar "
                    "com o amor."
                ),
                "preco": Decimal("41.90"),
                "estoque": 6,
                "ano": 1811,
                "autores": ["Jane Austen"],
                "categoria": "Romance",
                "editora": "Record",
            },
            {
                "titulo": "A Hora da Estrela",
                "isbn": "9780000000009",
                "descricao": (
                    "Romance de Clarice Lispector que acompanha "
                    "a trajetória de Macabéa."
                ),
                "preco": Decimal("37.90"),
                "estoque": 11,
                "ano": 1977,
                "autores": ["Clarice Lispector"],
                "categoria": "Literatura Brasileira",
                "editora": "Rocco",
            },
            {
                "titulo": "Perto do Coração Selvagem",
                "isbn": "9780000000010",
                "descricao": (
                    "Primeiro romance de Clarice Lispector, "
                    "centrado na subjetividade e nos conflitos "
                    "interiores da protagonista."
                ),
                "preco": Decimal("45.90"),
                "estoque": 4,
                "ano": 1943,
                "autores": ["Clarice Lispector"],
                "categoria": "Literatura Brasileira",
                "editora": "Rocco",
            },
            {
                "titulo": "Crime e Castigo",
                "isbn": "9780000000011",
                "descricao": (
                    "Romance psicológico sobre culpa, moralidade "
                    "e redenção."
                ),
                "preco": Decimal("59.90"),
                "estoque": 6,
                "ano": 1866,
                "autores": ["Fiódor Dostoiévski"],
                "categoria": "Filosofia",
                "editora": "Editora 34",
            },
            {
                "titulo": "Os Irmãos Karamázov",
                "isbn": "9780000000012",
                "descricao": (
                    "Romance filosófico que aborda fé, liberdade, "
                    "moralidade e conflitos familiares."
                ),
                "preco": Decimal("69.90"),
                "estoque": 3,
                "ano": 1880,
                "autores": ["Fiódor Dostoiévski"],
                "categoria": "Filosofia",
                "editora": "Editora 34",
            },
            {
                "titulo": "Capitães da Areia",
                "isbn": "9780000000013",
                "descricao": (
                    "Romance brasileiro que acompanha um grupo "
                    "de crianças e adolescentes em situação de rua."
                ),
                "preco": Decimal("39.90"),
                "estoque": 8,
                "ano": 1937,
                "autores": ["Jorge Amado"],
                "categoria": "Literatura Brasileira",
                "editora": "Companhia das Letras",
            },
            {
                "titulo": "Gabriela, Cravo e Canela",
                "isbn": "9780000000014",
                "descricao": (
                    "Romance ambientado na Bahia que acompanha "
                    "Gabriela e as transformações sociais de Ilhéus."
                ),
                "preco": Decimal("47.90"),
                "estoque": 5,
                "ano": 1958,
                "autores": ["Jorge Amado"],
                "categoria": "Romance",
                "editora": "Record",
            },
            {
                "titulo": "Frankenstein",
                "isbn": "9780000000015",
                "descricao": (
                    "Romance gótico sobre Victor Frankenstein "
                    "e a criatura que ele traz à vida."
                ),
                "preco": Decimal("36.90"),
                "estoque": 10,
                "ano": 1818,
                "autores": ["Mary Shelley"],
                "categoria": "Ficção Científica",
                "editora": "Penguin",
            },
            {
                "titulo": "O Pequeno Príncipe",
                "isbn": "9780000000016",
                "descricao": (
                    "Obra que acompanha um pequeno príncipe "
                    "em suas viagens por diferentes planetas."
                ),
                "preco": Decimal("32.90"),
                "estoque": 20,
                "ano": 1943,
                "autores": ["Antoine de Saint-Exupéry"],
                "categoria": "Infantojuvenil",
                "editora": "Intrínseca",
            },
            {
                "titulo": "Cem Anos de Solidão",
                "isbn": "9780000000017",
                "descricao": (
                    "Romance que narra várias gerações da família "
                    "Buendía na cidade fictícia de Macondo."
                ),
                "preco": Decimal("54.90"),
                "estoque": 7,
                "ano": 1967,
                "autores": ["Gabriel García Márquez"],
                "categoria": "Romance",
                "editora": "Record",
            },
        ]

        for dados in livros:
            livro, criado = Livro.objects.get_or_create(
                isbn=dados["isbn"],
                defaults={
                    "titulo": dados["titulo"],
                    "descricao": dados["descricao"],
                    "preco": dados["preco"],
                    "estoque": dados["estoque"],
                    "ano_publicacao": dados["ano"],
                    "categoria": categorias[dados["categoria"]],
                    "editora": editoras[dados["editora"]],
                },
            )

            for nome_autor in dados["autores"]:
                livro.autores.add(autores[nome_autor])

            if criado:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Criado: {livro.titulo}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Já existe: {livro.titulo}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                "\nSeed da livraria concluído!"
            )
        )