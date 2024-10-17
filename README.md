# Gerenciador de Tarefas - Task Manager

Este projeto é uma aplicação web para controle de tarefas e registro de tempo de trabalho, desenvolvida utilizando o framework **Django**. O sistema permite o cadastro de tarefas, o registro de tempos associados a essas tarefas, e oferece funcionalidades de listagem com filtros.


# Pré-requisitos

## 1. Controle de versão (Git)
O projeto utiliza o **Git** para controle de versão. Você pode instalar o Git em distribuições Debian/Ubuntu com o seguinte comando:

```
sudo apt-get install git
```

Mais informações estão disponíveis na documentação oficial do [Git](https://git-scm.com/downloads/linux).

## 2. Banco de dados SQLite
O projeto utiliza o **SQLite** como mecanismo de banco de dados. Para trabalhar com SQLite diretamente da linha de comando, você pode instalar o pacote:

```
sudo apt install sqlite3
```

Mais informações sobre o SQLite podem ser encontradas no site oficial [SQLite](https://www.sqlite.org/index.html).

## 3. Ambiente Virtual (virtualenvwrapper)
Para isolar as dependências do projeto, é recomendado o uso de ambientes virtuais. Uma opção é o **virtualenvwrapper**. Instale-o com o pip:

```
pip install virtualenvwrapper

```
Para configurar e ativar um ambiente virtual, use os seguintes comandos:

### Criar um ambiente virtual:

```
mkvirtualenv <NOME_DA_VENV>

```
### Ativar o ambiente virtual:

```
workon <NOME_DA_VENV>
```
### Desativar o ambiente virtual:

```
deactivate
```


Mais detalhes podem ser encontrados na documentação oficial do [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/#introduction).

# Passos para rodar o sistema


## 1. Clonar o repositório
Clone o repositório diretamente do **GitHub**. O código-fonte está disponível no seguinte endereço: [https://github.com/marcoshiroshi/taskmanager](https://github.com/marcoshiroshi/taskmanager)

para clonar o projeto, no terminal, digite uma das opções:

Via SSH:

```
git clone git@github.com:marcoshiroshi/taskmanager.git

```
Via HTTPS:

```
git clone https://github.com/marcoshiroshi/taskmanager.git
```

## 2. Instalar as dependências
Acesse a **raiz do projeto clonado** e, com o **ambiente virtual ativado**, instale as dependências necessárias (como Django e outras bibliotecas) usando o arquivo requirements.txt:

```
pip install -r requirements.txt
```

## 3. Rodar as migrações do banco de dados
Após instalar as dependências, rode as migrações do banco de dados para configurar as tabelas iniciais:

```
python manage.py migrate
```
## 4. Inserir dados iniciais no banco
Rode o script SQL para inserir dados adicionais no banco de dados SQLite:

```
sqlite3 db.sqlite3 < initial_sql.sql
```


## 5. Executando o projeto
Com tudo configurado, você pode iniciar o servidor localmente com o seguinte comando:

```
python manage.py runserver
```

Abra o navegador e acesse o endereço:


http://127.0.0.1:8000

Agora você pode usar o sistema localmente para gerenciar suas tarefas e tempos de trabalho.
