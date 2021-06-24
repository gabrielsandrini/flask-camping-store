# OUTDOOR IN-TENTS

Projeto de uma loja de equipamentos de camping desenvolvida no 5 semestre do curso de Análise e Desenvolvimento de Sistemas.

Integrantes:
- Gabriel Albinati Sandrini BP300508-9
- Letícia Mayara Soares Fernandes BP300511-9

Técnologias utilizadas:

- Flask
- HTML
- CSS
- JS

# Passos para executar o projeto

1 - Crie a venv: python3 -m venv venv
2 - ative a venv: source venv/bin/activate
Para desativar a venv: deactivate

instale o flask:
./setup.sh

Para rodar o projeto:
export FLASK_ENV=development
(para windows: set FLASK_ENV=development)
python3 **init**.py

### Migrations

python3 migrate.py db init
python3 migrate.py db migrate

### Se a migração falhar

python3 migrate.py db stamp head # To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
python3 migrate.py db migrate # To detect automatically all the changes.
python3 migrate.py db upgrade # To apply all the changes.
