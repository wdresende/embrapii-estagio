# embrapii-estagio
EMBRAPII - Processo Seletivo 002/2020


Micro Projeto para registro de pacientes que realizaram o teste de covid-19.

## Rodar a Aplicação

Para rodar a aplicação é preciso realizar primeiro a ativação do Ambiente Virtual:

``` source venv/bin/activate ```

Inicie a Aplicação rodando o seguinte comando:

``` python manage.py runserver ```

## Checando as rotas para CRUD:

### Rota para listar todos os testes dos pacientes:

http://localhost:8000/update/1

### Rota para adicionar um test: 

http://localhost:8000/create

### Rota para Atualizar ou excluir um teste cadastrado:

http://localhost:8000/update/id

Obs: Substituir id pelo o id do teste cadastrado
