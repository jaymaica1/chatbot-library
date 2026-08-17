from google import genai


client = genai.Client()


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Diga apenas: A conexão com o Gemini funcionou!"
)

print(response.text)