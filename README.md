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
```http
  POST /api/v1/auth/login
```
| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Obrigatório**. nome de usuário que foi cadastrado no sistema |
| `password` | `string` | **Obrigatório**. senha cadastrada para esse usuario |

```http
  POST /api/v1/auth/refresh
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `refresh_token` | `string`   | **Obrigatório**. O refresh token que foi retornado ao realizar login. |

### User (requer autenticação)
```http
  GET /api/v1/users/
```
Retorna todos os usuários ativos que estão cadastrados no sistema


