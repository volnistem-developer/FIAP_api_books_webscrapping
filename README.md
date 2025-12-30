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
