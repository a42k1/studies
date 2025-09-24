1 - Criar ambiente virtual
python -m venv venv

2 - Ativar ambiente virtual
.\venv\Scripts\activate

3 - Instalar django
pip install django

4 - Criar o arquivo de texto com as dependências
pip freeze > requirements.txt

5 - Criar base (Núcleo) do projeto
django-admin startproject core .

6 - RUN THE SERVER
python manage.py runserver

OBS>: About DB

make migrations (prepara o banco) criando as migrações

migrate (joga no banco) começa a migração
python manage.py migrate
