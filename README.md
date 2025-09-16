# Case-AutoU
Aplicação web desenvolvida para o Case Prático da AutoU.  O sistema classifica emails em "Produtivo" ou "Improdutivo"  e sugere respostas automáticas utilizando Flask, NLP e integração com IA.

##  Sobre o Projeto
A aplicação é uma solução web desenvolvida como case técnico que utiliza IA e  NLP para analisar o conteúdo de e-mails enviados pelos usuários.

A aplicação decide se um e-mail é Produtivo ou Improdutivo, utilizando conceitos de lematização e stopwords.
Além disso, os resultados são salvos em um banco de dados local (via SQLAlchemy) e exibidos em uma interface inspirada no Gmail, para facilitar a usabilidade.

## Funcionalidades
Envio de e-mails simulados pela interface (com texto e/ou anexos em PDF/TXT).

Classificação automática por IA (Produtivo ou Improdutivo).

Armazenamento em banco local com SQLAlchemy.

Visualização dos e-mails enviados em tabela estilo Gmail.

Gerenciamento de lixeira:

Restaurar e-mails da lixeira.

Excluir definitivamente (remove do banco e da pasta de uploads).

Suporte a anexos (.pdf e .txt) com leitura de conteúdo para análise.

## Tecnologias Utilizadas

### Backend
Python(Flask) 3.11+

SQLAlchemy

NLP:
spaCy
 – lematização e stopwords
Funções de pré-processamento de texto

### Frontend
HTML5 + CSS3

JavaScript 


## Observações:
Para rodar o Script após clonar, é preciso criar uma variável de ambiente chamada "OPENAI_KEY" com a chave da IA do OpenAI.