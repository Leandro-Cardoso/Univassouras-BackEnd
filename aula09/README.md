# Aula 09

[**<- VOLTAR**](https://github.com/Leandro-Cardoso/Univassouras-BackEnd)

## Conteúdo:
* **ForeignKey** unica e composta.
* **ACID** (Atomicidade, Consistencia, Isolamento e Durabilidade)
* **Django Shell** (metodo **seed** para inserir dados no banco).
<pre><code>
python manage.py shell

from todos.models import Category

# Criando categorias de exemplo
Category.objects.create(name="Trabalho")
Category.objects.create(name="Estudos")
Category.objects.create(name="Pessoal")

# Conferir se as categorias foram criadas
Category.objects.all()

exit()
</code></pre>
* Extensão **MySQL** para conexão e edição dos bancos de dados.

<br>

[**<- VOLTAR**](https://github.com/Leandro-Cardoso/Univassouras-BackEnd)
