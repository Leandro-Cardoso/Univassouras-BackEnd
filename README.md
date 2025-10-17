# Back End (Univassouras)
Estudo de Back End, com Python e Django.

<br>

## Aulas:

<br>

* [**Aula 02** - Ambiente de desenvolvimento e Django](https://github.com/Leandro-Cardoso/Univassouras-BackEnd/tree/main/aula02)
* [**Aula 03** - Models, migrations, urls e templates](https://github.com/Leandro-Cardoso/Univassouras-BackEnd/tree/main/aula03)
* [**Aula 04** - View e create](https://github.com/Leandro-Cardoso/Univassouras-BackEnd/tree/main/aula04)
* [**Aula 05** - Revisão](https://github.com/Leandro-Cardoso/Univassouras-BackEnd/tree/main/aula05)

<br>

* [**P1**](https://github.com/Leandro-Cardoso/Univassouras-BackEnd/tree/main/p1)

<br>

* [**Aula 06** - Update e revisão](https://github.com/Leandro-Cardoso/Univassouras-BackEnd/tree/main/aula06)
* [**Aula 07** - Delete e o Programador Pragmatico](https://github.com/Leandro-Cardoso/Univassouras-BackEnd/tree/main/aula07)

<br>

## Iniciando um novo projeto Django:

<br>

* Criar ambiente de desenvolvimento:
```[cmd]
python -m venv .venv
```

<br>

* Ativar ambiente criado:
```[cmd]
.venv\Scripts\activate
```

<br>

* Instalar biblioteca Django:
```[cmd]
pip install django
```

<br>

* Criar projeto Django:
```[cmd]
django-admin startproject setup .
```

<br>

* Criar app:
```[cmd]
python manage.py startapp NOME_DO_APP
```

<br>

* Fazer migrações:
```[cmd]
python manage.py makemigrations
python manage.py migrate
```

<br>

* Ligar servidor:
```[cmd]
python manage.py runserver
```

<br>

* Abrir projeto:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Dependencias:

<br>

* Cria arquivo com dependencias:
```[cmd]
pip freeze > requirements.txt
```

<br>

* Instala todas as dependencias:
```[cmd]
pip install -r requirements.txt
```
