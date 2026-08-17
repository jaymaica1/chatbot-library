from chatbot.services.gemini_service import interpretar_pergunta


perguntas = [
    "Quero um livro de fantasia por menos de 50 reais",
    "Vocês têm livros do Tolkien?",
    "Quero livros disponíveis de Machado de Assis",
]


for pergunta in perguntas:

    resultado = interpretar_pergunta(pergunta)

    print("\nPergunta:")
    print(pergunta)

    print("\nInterpretação:")
    print(resultado)