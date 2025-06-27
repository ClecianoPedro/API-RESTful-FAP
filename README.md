# 📡 API RESTful de Usuários - FAP

Este é um projeto de uma **API RESTful** construída em **Python com Flask**, organizada em **camadas (Controller, Service, Repository, Model)**. A API permite **cadastrar, listar todos os usuários, buscar por id, atualizar dados e deletar usuários**, persistindo os dados em um arquivo `JSON`.

---

## 🧱 Estrutura do Projeto

```
API-RESTful-FAP/
├── app.py
├── config.py
├── controller/
│   └── user_controller.py
├── service/
│   └── user_service.py
├── repository/
│   └── user_repository.py
├── model/
│   └── user.py
├── utils/
│   ├── functions.py
│   └── load_user_data.py
├── data/
│   └── users.json
├── requirements.txt
└── README.md
```

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Flask
- Flask-CORS
- email-validator

---

## 📌 Requisitos

- Python 3 instalado
- Ambiente virtual (recomendado)
- `pip` para instalar dependências

---

## ⚙️ Instalação e Execução

# Clone o projeto
git clone https://github.com/ClecianoPedro/API-RESTful-FAP.git

# Crie um ambiente virtual (opcional)
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python app.py

## 📚 Endpoints da API

# ✅ Criar usuário
POST /usuarios
```
json
{
  "name": "Exemplo",
  "email": "exemplo@gmail.com"
}
```
# 🔍 Buscar usuário por ID
GET /usuarios/<id>

# 📩 Buscar todos usuários
GET /usuarios

# 🛠️ Atualizar usuário
PUT /usuarios/<id>
```
json
{
  "name": "Exemplo Atualizado",
  "email": "novo_email@gmail.com"
}
```
❌ Deletar usuário
DELETE /usuarios/<id>

## 🧪 Validações
E-mail validado conforme RFC 5322 e DNS real.

Nome sem números ou caracteres especiais.

Prevenção contra duplicidade de e-mail.

## 🗃️ Persistência
Os dados dos usuários são armazenados em data/users.json, usando leitura e escrita via módulo utilitário.
