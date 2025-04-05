# Carteira API

API REST desenvolvida com Django e Django REST Framework. Possui autenticação JWT, gerenciamento de usuários e carteiras, transferências entre usuários e listagem de transações com filtro por data.

---

## 🚀 Tecnologias utilizadas  

- Python 3.11  
- Django 4.x  
- Django REST Framework  
- PostgreSQL  
- JWT  

## ⚙️ Como rodar o projeto

### 1. Clone o repositório  

git clone https://github.com/seu-usuario/seu-repositorio.git  
cd seu-repositorio  

### 2. Crie e ative o ambiente virtual  

python -m venv venv
source venv/bin/activate No linux 
venv\Scripts\activate # No Windows

### 3. Instale as dependências  

pip install -r requirements.txt

### 4. Configure o banco PostgreSQL  
No terminal:

sudo -u postgres psql

CREATE DATABASE wallet_db;
CREATE USER wallet_user WITH PASSWORD 'senha123';
GRANT ALL PRIVILEGES ON DATABASE wallet_db TO wallet_user;
\q

### 5. Configure o banco no arquivo config/settings.py  

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carteira_db',
        'USER': 'carteira_user',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 6. Rode as migrações  

python manage.py makemigrations
python manage.py migrate

### 7. Crie um superusuário    

python manage.py createsuperuser  

### 8. Popule o banco com dados de exemplo (opcional)

python manage.py shell < populate.py

### 9. Rode o servidor  

python manage.py runserver

### Endpoints

Registro	      POST	  /auth/users/  
Login (JWT)	    POST	  /auth/jwt/create/  
Saldo	          GET	    /api/wallet/saldo/  
Adicionar    	  POST	  /api/wallet/depositar/
Transferência	  POST	  /api/wallet/transferir/  
Transações	    GET	    /api/wallet/transactions/?start=&end=  

### Usuários de teste (via populate.py)
user1@example.com / senha123  
user2@example.com / senha123
user3@example.com / senha123
