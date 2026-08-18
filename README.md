# chatbot-library
Chatbot para livraria

git clone git@github.com:jaymaica1/chatbot-library.git

cd chatbot-library

docker compose up -d

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

python manage.py migrate

python manage.py seed_books

python manage.py runserver
