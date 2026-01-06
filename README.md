## Descrição do Projeto
O _FIAP_api_books_webscrapping_ é um projeto de API voltado para raspagem e disponibilização de dados do site educacional [Books to Scrape](https://books.toscrape.com/), desenvolvido com fins acadêmicos e didáticos.

O objetivo principal do projeto é demonstrar, na prática, conceitos como web scraping, estruturação de APIs, organização em camadas, tratamento de dados e boas práticas de desenvolvimento backend, servindo como apoio ao aprendizado proposto pela instituição de ensino FIAP.

Este repositório foi desenvolvido por Iuri Sanches Volnistem e possui caráter estritamente institucional, não tendo, até o momento, qualquer finalidade comercial. O uso dos dados extraídos é restrito a estudos, testes e demonstrações técnicas, respeitando o contexto educacional da aplicação.

## Arquitetura do Projeto
A arquitetura do projeto foi pensada com foco em escalabilidade, legibilidade de código e manutenibilidade. Ela é baseada nos princípios da Clean Architecture, amplamente utilizada no ecossistema .NET, com a qual possuo maior familiaridade.
A partir dessa abordagem, buscou-se aplicar as melhores práticas de organização em camadas, promovendo um código limpo, desacoplado e de fácil evolução.
A estrutura do projeto está organizada da seguinte forma:

```
FIAP_api_books_webscrapping/
├── public/                             # Arquivos públicos (ex: imagens dos livros)
│
├── src/                                # Código-fonte da aplicação
│   ├── api/                            # Camada de API (FastAPI)
│   │   ├── config/                     # Injeção de dependências e configs da API
│   │   ├── controllers/                # Controllers (endpoints)
│   │   │   └── v1/                     # Versionamento da API
│   │   ├── middlewares/                # Middlewares (ex: autenticação)
│   │   └── service/                    # Serviços da API (ponte entre controller e application)
│   │
│   ├── anticorruption/                 # Anti-Corruption Layer (integrações externas)
│   ├── application/                    # Camada de aplicação (casos de uso)
│   ├── data/                           # Configuração e acesso a dados
│   │   └── database/                   # Setup do banco de dados e ORM
│   ├── domain/                         # Domínio (regras de negócio)
│   ├── dtos/                           # Data Transfer Objects (entrada/saída)
│   ├── entity/                         # Entidades de persistência (ORM)
│   ├── exceptions/                     # Exceções customizadas
│   ├── infraestrutura/                 # Camada de infraestrutura
│   │   ├── config/                     # Configurações gerais
│   │   │   ├── pydantic/               # Configurações personalizadas de resposta do pydantic
│   │   │   ├── jwt_security.py         # Segurança JWT
│   │   │   └── env_config.py           # Variáveis de ambiente
│   │   ├── logging/                    # Configuração de logs
│   │   └── repository/                 # Implementações de repositórios
│   └── interfaces/                     # Interfaces e contratos
│       ├── application/                # Interfaces da camada application
│       ├── domain/                     # Interfaces do domínio
│       ├── infrastructure/             # Interfaces de infraestrutura
│       └── service/                    # Interfaces de serviço
│
├── main.py                             # Bootstrap da aplicação FastAPI
├── storage.db                          # Banco de dados SQLite
└── requirements.txt                    # Dependências do projeto
```

## Instalação e Configuração do Projeto
Após clonar o repositório para sua máquina, será necessário configurar um ambiente virtual Python e instalar as dependências do projeto antes de executá-lo.

Pré-requisitos
- Python instalado
- Sistema operacional Windows

> ⚠️ As instruções abaixo foram testadas exclusivamente em ambiente Windows.
Não há, até o momento, validação oficial para macOS ou Linux.

### Criação e ativação do ambiente virtual:
- Instale a biblioteca responsável pela criação do ambiente virtual:
  <pre>pip install virtualenv</pre>
- Crie o ambiente virtual (o nome venv é apenas uma sugestão):
  <pre>python -m virtualenv venv</pre>
- Ative o ambiente virtual de acordo com o terminal utilizado:
  <pre>.\venv\Scripts\Activate.ps1</pre> (caso esteja utilizando o powershell)
  <pre>.\venv\Scripts\activate.bat</pre> (caso esteja utilizando o cmd)

### Com o ambiente virtual ativo, instale as dependências do projeto:
  <pre>pip install -r requirements.txt</pre>

### Configuração das variáveis de ambiente
Para que a aplicação funcione corretamente, é necessário configurar o arquivo de variáveis de ambiente.

Na raiz do projeto, existe um arquivo chamado env.example.
Renomeie esse arquivo para .env e preencha os valores conforme necessário.

```
JWT_SECRET_KEY="sua_string_secreta"               
JWT_ALGORITHM="HS256"                             
DB_PATH="sqlite:///storage.db"                    
URL_TO_SCRAPE="https://books.toscrape.com/"       
SCRAPING_COOLDOWN_MINUTES=60 
```
#### Descrição das variáveis

> ###### JWT_SECRET_KEY
> Chave secreta utilizada para a criptografia do JWT.
> Recomenda-se gerar uma chave segura, por exemplo utilizando:
https://jwtsecrets.com/

> ###### JWT_ALGORITHM
> Algoritmo de criptografia do JWT.
> O valor padrão (HS256) é suficiente para o funcionamento do projeto.

> ###### DB_PATH
> Caminho de conexão com o banco de dados.
> O projeto utiliza SQLite, portanto não é necessário alterar esse valor.

> ###### URL_TO_SCRAPE
> URL base do site utilizado para a raspagem de dados.
> Não é necessário modificar esse valor.

> ###### SCRAPING_COOLDOWN_MINUTES
> Intervalo mínimo (em minutos) para permitir uma nova execução do processo de scraping.
> O valor padrão é 60 minutos, mas pode ser ajustado conforme a necessidade.

### Excecução do projeto
Para executar o projeto localmente em sua máquina utilize o comando:
  <pre>fastapi dev main.py</pre>

## Rotas da API

### Authorization

#### Login
```http
  POST /api/v1/auth/login
```
| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Obrigatório**. nome de usuário que foi cadastrado no sistema |
| `password` | `string` | **Obrigatório**. senha cadastrada para esse usuario |

> Possiveis Respostas
### Successful Response - 200
```http
  {
    "access_token": "string",
    "refresh_token": "string",
    "expires_in": 0
  }
```
### Not Found - 404
```http
{
  "message": "string"
}
```

### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

#### Refresh Token
```http
  POST /api/v1/auth/refresh
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `refresh_token` | `string`   | **Obrigatório**. O refresh token que foi retornado ao realizar login. |

> Possiveis Respostas
### Successful Response - 200
```http
{
  "access_token": "string",
  "refresh_token": "string",
  "expires_in": 0
}
```
### Unauthorized - 401
```http
{
  "message": "string"
}
```

### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

### User (requer autenticação)

#### Get all users
```http
  GET /api/v1/users/
```
> Possiveis Respostas
### Successful Response - 200
```http
[
  {
    "id": 0,
    "name": "string",
    "username": "string",
    "email": "string",
    "created_at": "2026-01-06T18:20:46.000Z",
    "active": true
  }
]
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```

#### Get specific user
```http
  GET /api/v1/users/{id}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id` | `int`| **Obrigatório**. Id do usuário que deseja procurar.      |


> Possiveis Respostas

### Successful Response - 200
```http
{
  "id": 0,
  "name": "string",
  "username": "string",
  "email": "string",
  "created_at": "2026-01-06T21:40:29.387Z",
  "active": true
}
```
### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
### Not Found - 404
```http
{
  "message": "string"
}
```

#### Insert new user (Não precisa estar autenticado)
```http
  POST /api/v1/users/
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `name` | `string`| **Obrigatório**. Nome do usuário      |
| `username` | `string`| **Obrigatório**. username para o usuário (unique constraint)      |
| `email` | `string`| **Obrigatório**. e-mail do usuário (unique constraint)      |
| `password` | `string`| **Obrigatório**. senha para o usuário      |

> Possiveis Respostas

### Successful Response - 201
```http
{
  "id": 0,
  "name": "string",
  "username": "string",
  "email": "string",
  "created_at": "2026-01-06T18:21:47.450Z",
  "active": true
}
```
### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
### Bad Request - 400
```http
{
  "message": "string"
}
```


#### Delete a user
```http
  DELETE /api/v1/users/{id}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id` | `int`| **Obrigatório**. Id do usuário que deseja inativar       |

> Possiveis Respostas

### Successful Response - 200
```http
{
  "id": 0,
  "name": "string",
  "username": "string",
  "email": "string",
  "created_at": "2026-01-06T21:40:29.387Z",
  "active": true
}
```
### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
### Not Found - 404
```http
{
  "message": "string"
}
```

#### Update a user
```http
  PUT /api/v1/users/{id}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id` | `int`| **Obrigatório**. Id do usuário que deseja atualizar      |


> Possiveis Respostas

### Successful Response - 200
```http
{
  "id": 0,
  "name": "string",
  "username": "string",
  "email": "string",
  "created_at": "2026-01-06T21:40:29.387Z",
  "active": true
}
```
### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
### Not Found - 404
```http
{
  "message": "string"
}
```


### Scraping (requer autenticação)

#### Start scraping
```http
  POST /api/v1/scraping/trigger
```

> Possiveis Respostas

### Successful Response - 200
```http
{
    "status": 'string',
    "message": 'string'
}
```

#### Get scraping Status
```http
  GET /api/v1/scraping/status
```
> Possiveis Respostas

### Successful Response - 200
```http
{
  "status": "string",
  "started_at": "2026-01-06T22:01:20.567Z",
  "finished_at": "2026-01-06T22:01:20.567Z",
  "error": "string"
}
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```

### Books (requer autenticação)

#### Get all Books
```http
  GET /api/v1/books
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `page` | `int`| **Default = 1**. Página atual para a visualização dos livros       |
| `page_size` | `int`| **Default = 10**. Quantidade de livros aprensentada na página atual       |

> Possiveis Respostas

### Successful Response - 200
```http
{
  "page": 0,
  "page_size": 0,
  "total_of_books": 0,
  "total_of_pages": 0,
  "catalog": [
    {
      "id": 0,
      "title": "string",
      "slug": "string",
      "rating": 0,
      "raw_price_in_cents": 0,
      "raw_price": 0,
      "brl_price_in_cents": 0,
      "brl_price": 0,
      "image_path": "string",
      "available": true,
      "categories": [
        {
          "id": 0,
          "name": "string"
        }
      ]
    }
  ]
}
```
### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```

#### Get Books by title and/or category
```http
  GET /api/v1/books/search
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `title` | `string`|  Titulo que deseja filtrar       |
| `category` | `string`| Categoria que deseja filtrar       |


> Possiveis Respostas

### Successful Response - 200
```http
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "rating": 0,
    "raw_price_in_cents": 0,
    "raw_price": 0,
    "brl_price_in_cents": 0,
    "brl_price": 0,
    "image_path": "string",
    "available": true,
    "categories": [
      {
        "id": 0,
        "name": "string"
      }
    ]
  }
]
```
### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```

#### Get Books by Price Range
```http
  GET /api/v1/books/price-range
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `min` | `float`| **Obrigatório**. Valor minimo para o range de preços  |
| `max` | `float`| **Obrigatório**. Valor máximo para o range de preços  |

> Possiveis Respostas

### Successful Response - 200
```http
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "rating": 0,
    "raw_price_in_cents": 0,
    "raw_price": 0,
    "brl_price_in_cents": 0,
    "brl_price": 0,
    "image_path": "string",
    "available": true,
    "categories": [
      {
        "id": 0,
        "name": "string"
      }
    ]
  }
]
```
### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```

#### Get specific Book
```http
  GET /api/v1/books/{id}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id` | `int`| **Obrigatório**. Id do livro que deseja procurar         |

> Possiveis Respostas

### Successful Response - 200
```http
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "rating": 0,
  "raw_price_in_cents": 0,
  "raw_price": 0,
  "brl_price_in_cents": 0,
  "brl_price": 0,
  "image_path": "string",
  "available": true,
  "categories": [
    {
      "id": 0,
      "name": "string"
    }
  ]
}
```
### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```
### Not Found - 404
```http
{
  "message": "string"
}
```

#### List all Categories
```http
  GET /api/v1/books/categories
```

> Possiveis Respostas

### Successful Response - 200
```http
[
  {
    "id": 0,
    "name": "string"
  }
]
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```

#### Get Top-rated Books (only books with 5 stars rating) 
```http
  GET /api/v1/books/top-rated
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `page` | `int`| **Default = 1**. Página atual para a visualização dos livros       |
| `page_size` | `int`| **Default = 10**. Quantidade de livros aprensentada na página atual       |

> Possiveis Respostas

### Successful Response - 200
```http
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "rating": 0,
  "raw_price_in_cents": 0,
  "raw_price": 0,
  "brl_price_in_cents": 0,
  "brl_price": 0,
  "image_path": "string",
  "available": true,
  "categories": [
    {
      "id": 0,
      "name": "string"
    }
  ]
}
```
### Validation Error (pydantic) - 422
```http
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```

### Health
#### Check API connectivity
```http
  GET /api/v1/health
```

> Possiveis Respostas

### Successful Response - 200
```http
{
  "status": "ok",
  "api": "up",
  "database": "up",
  "timestamp": "2026-01-06T22:01:20.567Z"
}
```

### Statistics (Requer autenticação)

#### Get overview
```http
  GET /api/v1/stats/overview
```

> Possiveis Respostas

### Successful Response - 200
```http
{
  "total_books": 0,
  "available_books": 0,
  "unavailable_books": 0,
  "average_rating": 0,
  "average_price_brl": 0,
  "last_scrap_execution": "2026-01-06T22:16:09.111Z"
}
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```

#### Get Statistics from categories
```http
  GET /api/v1/stats/categories
```
### Successful Response - 200
```http
[
  {
    "category": "string",
    "total_books": 0,
    "available_books": 0,
    "average_rating": 0,
    "average_price_brl": 0
  }
]
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```

#### Get Statistics from Availability
```http
  GET /api/v1/stats/availability
```
### Successful Response - 200
```http
{
  "total_books": 0,
  "available_books": 0,
  "unavailable_books": 0,
  "availability_rate": 0
}
```
### Unauthorized - 401 (Se não estiver autenticado)
```http
{
  "message": "string"
}
```
