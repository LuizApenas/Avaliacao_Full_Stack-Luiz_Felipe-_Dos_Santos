# 🚀 Guia Completo de Instalação - Encurtador de URL

Este guia é para instalar o projeto em uma **máquina limpa sem Python** ou com problemas de dependências.

## 📋 Pré-requisitos

### 1. **Instalar Python 3.11 ou 3.12**
- ⚠️ **IMPORTANTE**: Não use Python 3.13 (ainda tem problemas de compatibilidade)
- Baixe do site oficial: https://www.python.org/downloads/
- Durante a instalação, **marque "Add to PATH"**
- Teste no terminal: `python --version`

### 2. **Instalar Node.js (para o frontend)**
- Baixe do site oficial: https://nodejs.org/
- Versão recomendada: LTS (Long Term Support)
- Teste no terminal: `node --version` e `npm --version`

### 3. **Configurar MongoDB Atlas** (Banco de dados)
- Crie uma conta gratuita em: https://www.mongodb.com/atlas
- Crie um cluster gratuito
- Obtenha a string de conexão (MongoDB URI)

## 🔧 Instalação do Backend (Python)

### Opção 1: Script Automatizado (Recomendado)

```bash
# 1. Navegue até o diretório backend
cd "DesafioFullStack(Encurtador URL)/backend"

# 2. Execute o script de instalação
python install_dependencies.py

# OU no Windows:
install_dependencies.bat
```

### Opção 2: Instalação Manual (Caso o script falhe)

```bash
# 1. Navegue até o diretório backend
cd "DesafioFullStack(Encurtador URL)/backend"

# 2. Crie um ambiente virtual
python -m venv venv

# 3. Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Atualize pip e instale ferramentas
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel

# 5. Instale dependências em ordem específica (IMPORTANTE!)
python -m pip install "certifi>=2024.0.0" --prefer-binary --no-cache-dir
python -m pip install "idna>=3.4,<4.0" --prefer-binary --no-cache-dir
python -m pip install "sniffio>=1.3.0,<2.0.0" --prefer-binary --no-cache-dir
python -m pip install "click>=8.1.0,<9.0.0" --prefer-binary --no-cache-dir
python -m pip install "colorama>=0.4.6,<0.5.0" --prefer-binary --no-cache-dir

python -m pip install "typing-extensions>=4.8.0,<5.0.0" --prefer-binary --no-cache-dir
python -m pip install "annotated-types>=0.6.0,<0.8.0" --prefer-binary --no-cache-dir

python -m pip install "python-dotenv>=1.0.0,<1.1.0" --prefer-binary --no-cache-dir
python -m pip install "anyio>=4.0.0,<5.0.0" --prefer-binary --no-cache-dir

python -m pip install "h11>=0.14.0,<0.15.0" --prefer-binary --no-cache-dir
python -m pip install "httpcore>=1.0.0,<2.0.0" --prefer-binary --no-cache-dir
python -m pip install "httpx>=0.25.0,<0.27.0" --prefer-binary --no-cache-dir

python -m pip install "pydantic>=2.5.0,<3.0.0" --prefer-binary --no-cache-dir
python -m pip install "pydantic-settings>=2.1.0,<3.0.0" --prefer-binary --no-cache-dir

python -m pip install "starlette>=0.27.0,<0.29.0" --prefer-binary --no-cache-dir
python -m pip install "fastapi>=0.104.1,<0.106.0" --prefer-binary --no-cache-dir

python -m pip install "httptools>=0.6.0,<0.7.0" --prefer-binary --no-cache-dir
python -m pip install "python-multipart>=0.0.6,<0.1.0" --prefer-binary --no-cache-dir
python -m pip install "watchfiles>=0.21.0,<0.23.0" --prefer-binary --no-cache-dir
python -m pip install "websockets>=12.0,<14.0" --prefer-binary --no-cache-dir
python -m pip install "uvicorn[standard]>=0.24.0,<0.26.0" --prefer-binary --no-cache-dir

python -m pip install "pymongo>=4.6.0,<5.0.0" --prefer-binary --no-cache-dir
python -m pip install "motor>=3.3.0,<4.0.0" --prefer-binary --no-cache-dir
python -m pip install "beanie>=1.23.0,<2.0.0" --prefer-binary --no-cache-dir

python -m pip install "pytest>=7.4.0,<8.0.0" --prefer-binary --no-cache-dir
python -m pip install "pytest-asyncio>=0.21.0,<0.23.0" --prefer-binary --no-cache-dir
```

## 🎯 Instalação do Frontend (React)

```bash
# 1. Navegue até o diretório frontend
cd "DesafioFullStack(Encurtador URL)/frontend"

# 2. Instale as dependências
npm install

# 3. Execute o projeto (modo desenvolvimento)
npm run dev
```

## ⚙️ Configuração

### 1. **Configurar variáveis de ambiente**

Crie um arquivo `.env` no diretório `backend/` com:

```env
# MongoDB Atlas
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/
DATABASE_NAME=url_shortener

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Frontend URL (para CORS)
FRONTEND_URL=http://localhost:5173
```

### 2. **Substituir valores**
- `username:password` → suas credenciais do MongoDB Atlas
- `cluster.mongodb.net` → URL do seu cluster

## 🚀 Executar o Projeto

### 1. **Iniciar o Backend**

```bash
# Navegue até o backend
cd "DesafioFullStack(Encurtador URL)/backend"

# Ative o ambiente virtual (se não estiver ativo)
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Execute o servidor
python main.py

# OU usando uvicorn diretamente
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. **Iniciar o Frontend** (em outro terminal)

```bash
# Navegue até o frontend
cd "DesafioFullStack(Encurtador URL)/frontend"

# Execute o servidor de desenvolvimento
npm run dev
```

### 3. **Acessar a aplicação**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Documentação da API: http://localhost:8000/docs

## ✅ Verificar Instalação

### Teste do Backend:
```bash
cd backend
python -c "import fastapi, uvicorn, motor, beanie; print('✅ Backend OK!')"
```

### Teste do Frontend:
```bash
cd frontend
npm run build
```

## 🚨 Solução de Problemas Comuns

### 1. **Erro de compilação do pydantic-core**
```bash
# Instale o Microsoft C++ Build Tools
# https://visualstudio.microsoft.com/visual-cpp-build-tools/

# OU use apenas pacotes pré-compilados
python -m pip install --only-binary=all -r requirements.txt
```

### 2. **Erro "ModuleNotFoundError: No module named 'fastapi'"**
```bash
# Certifique-se de que o ambiente virtual está ativo
venv\Scripts\activate  # Windows
python -m pip list  # Verificar pacotes instalados
```

### 3. **Erro de conexão com MongoDB**
```bash
# Verifique se o IP está liberado no MongoDB Atlas
# Verifique se a string de conexão está correta no .env
# Teste a conexão manualmente
```

### 4. **Porta já em uso**
```bash
# Backend (mude a porta)
uvicorn main:app --reload --host 0.0.0.0 --port 8001

# Frontend (mude a porta)
npm run dev -- --port 5174
```

## 📊 Ordem de Dependências Explicada

### Por que esta ordem específica?

1. **Etapa 1-3**: Dependências base sem conflitos
2. **Etapa 4**: HTTP core (h11 → httpcore → httpx)
3. **Etapa 5**: Pydantic (antes do FastAPI)
4. **Etapa 6-7**: Starlette → FastAPI
5. **Etapa 8**: Servidor ASGI e ferramentas
6. **Etapa 9**: MongoDB (PyMongo → Motor → Beanie)
7. **Etapa 10**: Testes (por último)

### Flags importantes:
- `--prefer-binary`: Usa pacotes pré-compilados (evita Rust/C++)
- `--no-cache-dir`: Evita cache corrompido
- Versões específicas: Evita conflitos

## 🎉 Sucesso!

Se tudo funcionou, você deve ver:
- ✅ Backend rodando em http://localhost:8000
- ✅ Frontend rodando em http://localhost:5173  
- ✅ Banco MongoDB conectado
- ✅ API funcionando (teste em /docs)

---

**💡 Dica**: Sempre use o script automatizado primeiro. A instalação manual é apenas para casos específicos de erro.
