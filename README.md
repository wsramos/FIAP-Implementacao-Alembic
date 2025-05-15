# FIAP: Migração de Schemas com Alembic

Este projeto é um estudo sobre como realizar migrações de schemas em um banco de dados utilizando Flask, SQLAlchemy e Alembic.

## Introdução ao Alembic
O **Alembic** é uma ferramenta de migração de banco de dados para aplicações que utilizam o SQLAlchemy. Ele permite gerenciar alterações no esquema do banco de dados de forma eficiente e controlada, garantindo que as mudanças sejam aplicadas de maneira consistente em diferentes ambientes (desenvolvimento, teste e produção).

### Função
O Alembic é responsável por:

Criar, aplicar e reverter migrações no banco de dados.
Gerenciar versões do esquema do banco de dados.
Automatizar a geração de scripts de migração com base nos modelos definidos no SQLAlchemy.

### Vantagens
* Automação: Gera scripts de migração automaticamente com base nas alterações nos modelos.
* Controle de versão: Permite rastrear e reverter alterações no esquema do banco de dados.
* Flexibilidade: Suporta múltiplos bancos de dados e integra-se facilmente ao SQLAlchemy.
* Consistência: Garante que o esquema do banco de dados esteja sincronizado com os modelos da aplicação.

### Desvantagens
* Curva de aprendizado: Pode ser desafiador para iniciantes entender a configuração e o fluxo de trabalho.
* Dependência do SQLAlchemy: É projetado para funcionar exclusivamente com o SQLAlchemy, limitando seu uso em outros contextos.

O Alembic é uma ferramenta essencial para projetos que exigem controle rigoroso sobre as mudanças no banco de dados, especialmente em equipes de desenvolvimento colaborativo.

## Requirements
Certifique-se de ter os seguintes requisitos instalados antes de configurar o projeto:

* **Python 3.8 ou superior**: Para rodar o projeto e gerenciar dependências.
* **pip**: Gerenciador de pacotes do Python.
* **Virtualenv** (opcional, mas recomendado): Para criar ambientes isolados.
* **SQLite**: Banco de dados utilizado no projeto (já incluído na maioria das instalações do Python).

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalá-las, siga as instruções na seção Configuração do Ambiente Virtual.

## Configuração do Ambiente Virtual

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
    ```
2. Ative o ambiente virtual:

    Windows:
    ```bash
    venv\Scripts\activate
    ```
    Linux/Mac:
    ```
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração do Alembic

1. Inicialize o Alembic no projeto:
    ```bash
    alembic init alembic
    ```

2. Configure o arquivo alembic.ini:

    Altere a string de conexão para o banco de dados SQLite:
    ```python
    sqlalchemy.url = sqlite:///meu_banco.db
    ```

    Edite o arquivo env.py para incluir o objeto db.metadata:
    ```python
    from app import db
    from models import Usuario, Receita  # Importe os modelos

    target_metadata = db.metadata
    ```

## Criando uma Nova Migração
Gere uma nova migração automaticamente:
```bash
alembic revision --autogenerate -m "Descrição da migração"
```

Verifique o arquivo gerado em versions para garantir que as alterações estão corretas.

## Aplicando Migrações
Atualize o banco de dados para a última versão:
```bash
alembic upgrade head
```

Para reverter uma migração:
```bash
alembic downgrade -1
```
