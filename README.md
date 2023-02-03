Para ambiente linux.

Com do docker instaldo, caso não tenha -> https://docs.docker.com/engine/install/ e https://docs.docker.com/compose/install/

Para rodar a aplicação, no docker-compose.yml para subir um container.

    $ docker-compose up



Ou caso não tenha o docker instalado, mas será necessario ter o python instaldo, de preferencia a versão 3.10:
    
    1-Craindo o ambiente:
        $ python -m venv .venv

    2-Ativando o ambiente no linux:
        $ source .venv/bin/activate

    3-Instalando os requisitos:
        $ pip install -r requierements.txt

    4-para rodar o projeto, na raiz do projeto:
        $ python -m main


Acesse a documentação em http://0.0.0.0:8000/api/v1/doc ou http://0.0.0.0:8000/api/v1/redoc

E para gerar o toke é necessario cadastrar um user em http://0.0.0.0:8000/api/v1/users, passando no body o username e passaword:
- ex:

      curl -X 'POST' \
      'http://localhost:8000/api/v1/users' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "username": "Username",
      "password": "string"
      }'

Apos criar o usuario, gerar o token no endpoint http://0.0.0.0:8000/api/v1/users/token
 - ex:

       curl -X 'POST' \
       'http://0.0.0.0:8000/api/v1/users/token' \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d '{
       "username": "Username",
       "password": "string"
       }'
    
Resposta sera: 

            {
              "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmcyIiwiZXhwIjoxNjc1NDQwMzMwfQ.QJuP-1dHxYU1osmi4-P8e8U-Bnw3g5zVCGN9uYvH_oA",
              "token_type": "bearer"
            }


Para pode acessar os endpoint patients, pharmacies, transactions é necessario passar o token na requisição.

- Ex:

          curl -X 'GET' \
          'http://localhost:8000/api/v1/pharmacies' \
          -H 'accept: application/json' \
          -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJleHAiOjE2NzU0Mzg0OTd9._bq4MjvwrKu_MsE1LA9XW2kBgPitzwl2ri4svu984fY'

Mas na propria doc (http://0.0.0.0:8000/api/v1/doc) é possivel passar o token em autorization.



Endpoint:
 - http://0.0.0.0:8000/api/v1/users
 - http://0.0.0.0:8000/api/v1/patients
 - http://0.0.0.0:8000/api/v1/pharmacies
 - http://0.0.0.0:8000/api/v1/transactions