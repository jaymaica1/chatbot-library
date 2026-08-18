# chatbot-library
Chatbot para livraria
``` bash

docker compose up -d

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

python manage.py migrate

python manage.py seed_books

python manage.py runserver
```
For frontend:
``` bash
npm start
```
