from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=20, unique=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    ano_publicacao = models.PositiveIntegerField(null=True, blank=True)

    autores = models.ManyToManyField(
        Autor,
        related_name="livros"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="livros"
    )

    editora = models.ForeignKey(
        Editora,
        on_delete=models.PROTECT,
        related_name="livros"
    )

    def __str__(self):
        return self.titulo
