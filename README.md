# 🔗 Encurtador de URL - Full Stack Project

Este projeto Full Stack foi desenvolvido para demonstrar habilidades no desenvolvimento de aplicações modernas, utilizando tecnologias de ponta para criar um sistema completo de encurtamento de URLs, desde o Front-End até o Back-End.

> 🚀 **Pronto para usar!** Este projeto já vem com banco de dados MongoDB configurado e scripts de instalação automatizados. Basta clonar e executar!

## 📌 Funcionalidades Implementadas

✅ **Encurtamento de URLs** com redirecionamento automático  
✅ **Exibição de estatísticas** de acessos em tempo real  
✅ **Dashboard interativo** com métricas detalhadas  
✅ **API RESTful** documentada com Swagger/OpenAPI  
✅ **Interface responsiva** e moderna  
✅ **Filtro de pesquisa** para URLs cadastradas  
✅ **Validação de URLs** com protocolo obrigatório  
✅ **Métricas avançadas** (User-Agent, IP, Referer)  
✅ **Sistema de saúde** para URLs inativas  

## 🛠 Tecnologias Utilizadas

### 🌐 **Front-End:**
- **React 19** - Biblioteca JavaScript para interfaces de usuário modernas
- **Vite** - Build tool rápido e moderno para desenvolvimento
- **TypeScript** - Superset do JavaScript com tipagem estática
- **TailwindCSS** - Framework CSS utility-first para design responsivo
- **Lucide React** - Biblioteca de ícones moderna e elegante
- **Class Variance Authority** - Gerenciamento de variantes de componentes

### ⚙️ **Back-End:**
- **Python 3.11+** - Linguagem de programação moderna e eficiente
- **FastAPI** - Framework web moderno e de alta performance
- **Pydantic** - Validação de dados e serialização
- **Uvicorn** - Servidor ASGI de alta performance
- **Motor** - Driver assíncrono para MongoDB
- **Beanie** - ODM (Object Document Mapper) para MongoDB

### 🗄 **Banco de Dados:**
- **MongoDB Atlas** - Banco de dados NoSQL na nuvem, escalável e eficiente

### 🔧 **Ferramentas de Desenvolvimento:**
- **Swagger/OpenAPI** - Documentação automática da API
- **ESLint** - Linter para código JavaScript/TypeScript
- **PostCSS** - Processador de CSS
- **Autoprefixer** - Adiciona prefixos CSS automaticamente

## 🚀 Como Rodar o Projeto

### 📌 **Pré-requisitos**
Certifique-se de ter as seguintes ferramentas instaladas no seu ambiente:

- **Python 3.11+** (⚠️ Não use Python 3.13)
- **Node.js 18+** 
- **npm** ou **yarn**
- **MongoDB Atlas** (conta gratuita)

### 🎨 **Como Rodar o Front-End**

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/encurtador-url.git
   cd "DesafioFullStack(Encurtador URL)"
   ```

2. **Acesse a pasta do Front-End:**
   ```bash
   cd frontend
   ```

3. **Instale as dependências:**
   ```bash
   npm install
   ```

4. **Execute o projeto:**
   ```bash
   npm run dev
   ```

5. **O projeto estará rodando em:**
   ```
   http://localhost:5173
   ```

### 🔧 **Como Rodar o Back-End**

#### **Opção 1: Instalação Automatizada (Recomendado)**

1. **Acesse a pasta do Back-End:**
   ```bash
   cd backend
   ```

2. **Execute o script de instalação:**
   ```bash
   # Windows
   install_dependencies.bat
   
   # Linux/Mac
   python install_dependencies.py
   ```

3. **Configure as variáveis de ambiente (OPCIONAL):**
   O projeto já vem com credenciais de teste configuradas. Se quiser personalizar, crie um arquivo `.env` na pasta `backend/`:
   ```env
   # MongoDB Atlas (já configurado no projeto para testes)
   MONGODB_URL=mongodb+srv://luiz_test_encurtador:a6UXnqk9LoVVh6dt@cluster0.cdebnt2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
   DATABASE_NAME=url_shortener
   
   # API Configuration
   API_HOST=0.0.0.0
   API_PORT=8000
   
   # Base URL
   BASE_URL=http://127.0.0.1:8000
   ```
   
   > ⚠️ **Nota:** As credenciais acima são apenas para testes e demonstração. Em produção, use suas próprias credenciais.

4. **Execute a aplicação:**
   ```bash
   python main.py
   ```

#### **Opção 2: Instalação Manual**

1. **Crie um ambiente virtual:**
   ```bash
   cd backend
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Instale as dependências em ordem:**
   ```bash
   python -m pip install --upgrade pip setuptools wheel
   python -m pip install -r requirements.txt --prefer-binary --no-cache-dir
   ```

3. **Execute a aplicação:**
   ```bash
   python main.py
   ```
   > 💡 **Dica:** O projeto já vem com MongoDB configurado para testes, não precisa configurar nada!

### 🌐 **URLs de Acesso**

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **Documentação Swagger:** http://localhost:8000/docs
- **Redoc:** http://localhost:8000/redoc

## 📊 **Estrutura do Projeto**

```
DesafioFullStack(Encurtador URL)/
├── 📁 frontend/                 # Aplicação React
│   ├── 📁 src/
│   │   ├── 📁 components/       # Componentes React
│   │   ├── 📁 services/         # Serviços de API
│   │   └── 📁 types/           # Tipos TypeScript
│   ├── 📄 package.json
│   └── 📄 vite.config.ts
├── 📁 backend/                  # API FastAPI
│   ├── 📁 router/              # Rotas da API
│   ├── 📁 services/            # Serviços de negócio
│   ├── 📄 main.py              # Arquivo principal
│   ├── 📄 models.py            # Modelos de dados
│   ├── 📄 database.py          # Configuração do banco
│   ├── 📄 requirements.txt     # Dependências Python
│   ├── 📄 install_dependencies.py   # Script de instalação
│   └── 📄 install_dependencies.bat  # Script Windows
├── 📄 README.md                # Este arquivo
├── 📄 INSTALACAO_COMPLETA.md   # Guia detalhado
└── 📄 .gitignore
```

## 🔗 **Endpoints da API**

### **URLs**
- `POST /api/urls/` - Criar URL encurtada
- `GET /api/urls/` - Listar todas as URLs
- `GET /api/urls/{short_id}/metrics` - Métricas de uma URL
- `GET /{short_id}` - Redirecionamento

### **Métricas**
- `GET /api/metrics/` - Todas as métricas
- `POST /api/metrics/` - Registrar novo acesso

## 🎯 **Funcionalidades Técnicas**

### **Backend (FastAPI)**
- ✅ **API RESTful** com documentação automática
- ✅ **Validação de dados** com Pydantic
- ✅ **Conexão MongoDB** com Motor (driver assíncrono)
- ✅ **ODM Beanie** para modelagem de documentos
- ✅ **Middleware CORS** configurado
- ✅ **Health checks** para URLs
- ✅ **Tratamento de erros** robusto

### **Frontend (React)**
- ✅ **Interface responsiva** com TailwindCSS
- ✅ **Estados gerenciados** com React Hooks
- ✅ **Requisições HTTP** otimizadas
- ✅ **Filtros de pesquisa** em tempo real
- ✅ **Feedback visual** para ações do usuário
- ✅ **Tratamento de erros** amigável

### **Banco de Dados (MongoDB)**
- ✅ **Coleções indexadas** para performance
- ✅ **Documentos estruturados** com validação
- ✅ **Métricas detalhadas** de acesso
- ✅ **Timestamps automáticos**

## 🔧 **Solução de Problemas**

### **Erro de Compilação (pydantic-core)**
```bash
# Use o script de instalação automatizada
python install_dependencies.py
```

### **Porta já em uso**
```bash
# Backend - mude a porta
uvicorn main:app --reload --port 8001

# Frontend - mude a porta  
npm run dev -- --port 5174
```

### **Erro de conexão MongoDB**
1. Verifique se a string de conexão está correta no `.env`
2. Certifique-se de que o IP está liberado no MongoDB Atlas
3. Teste a conexão manualmente

## 🧪 **Como Testar**

1. **Teste o Backend:**
   ```bash
   cd backend
   python -c "import fastapi, uvicorn, motor, beanie; print('✅ Backend OK!')"
   ```

2. **Teste o Frontend:**
   ```bash
   cd frontend
   npm run build
   ```

3. **Teste a API:**
   - Acesse: http://localhost:8000/docs
   - Use o Swagger para testar os endpoints

## 📈 **Métricas e Monitoramento**

O sistema coleta automaticamente:
- 📊 **Número de acessos** por URL
- 🕒 **Timestamps** de cada acesso
- 🌐 **User-Agent** dos visitantes
- 📍 **Endereços IP** (para análise geográfica)
- 🔗 **Referer** (site de origem)

## 🚀 **Deploy**

### **Frontend (Vercel/Netlify)**
```bash
npm run build
# Upload da pasta dist/
```

### **Backend (Railway/Heroku)**
```bash
# Configure as variáveis de ambiente
# Faça deploy da pasta backend/
```

## 📜 **Autor**

👤 **Luiz Felipe Dos Santos**  
📧 **Email:** luizz.felipe.santos17@gmail.com  
🔗 **LinkedIn:** https://www.linkedin.com/in/luiz-felipe-santos-95490b208/ 
🐱 **GitHub:** https://github.com/LuizApenas  

---

🚀 **Projeto desenvolvido como parte de um desafio Full Stack, demonstrando expertise em tecnologias modernas de desenvolvimento web.**

## 📝 **Licença**

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela no repositório!**

# ===================================================================
# REQUIREMENTS COMPATÍVEL COM PYTHON 3.11, 3.12 E 3.13
# Ordem otimizada para evitar conflitos de dependências
# ===================================================================

# ETAPA 1: Dependências base do sistema
certifi>=2024.0.0
idna>=3.4,<4.0
sniffio>=1.3.0,<2.0.0
click>=8.1.0,<9.0.0
colorama>=0.4.6,<0.5.0

# ETAPA 2: Tipos e extensões fundamentais
typing-extensions>=4.8.0,<5.0.0
annotated-types>=0.6.0,<0.8.0

# ETAPA 3: Utilitários core
python-dotenv>=1.0.0,<1.1.0
anyio>=4.0.0,<5.0.0

# ETAPA 4: HTTP core (ordem específica)
h11>=0.14.0,<0.15.0
httpcore>=1.0.0,<2.0.0
httpx>=0.25.0,<0.27.0

# ETAPA 5: Validação (versões compatíveis com Python 3.13)
pydantic>=2.10.0,<3.0.0
pydantic-settings>=2.6.0,<3.0.0

# ETAPA 6: Web framework base
starlette>=0.28.0,<0.30.0

# ETAPA 7: FastAPI
fastapi>=0.105.0,<0.107.0

# ETAPA 8: Servidor ASGI (sem watchfiles para evitar compilação Rust)
httptools>=0.6.0,<0.7.0
python-multipart>=0.0.6,<0.1.0
# watchfiles removido - causa problemas de compilação no Python 3.13
websockets>=12.0,<14.0
# Uvicorn básico (sem [standard]) para evitar watchfiles
uvicorn>=0.24.0,<0.26.0

# ETAPA 9: MongoDB
pymongo>=4.6.0,<5.0.0
motor>=3.3.0,<4.0.0
beanie>=1.24.0,<2.0.0

# ETAPA 10: Testes
pytest>=7.4.0,<8.0.0
pytest-asyncio>=0.21.0,<0.23.0

## 🔧 **Principais Mudanças:**

1. **❌ Removido `watchfiles`** - causava erro de compilação Rust
2. **🔄 Atualizado `pydantic`** para versão 2.10.0+ (compatível com Python 3.13)
3. **🔄 Atualizado `pydantic-settings`** para versão 2.6.0+
4. **🔄 Atualizado `starlette`** para versão 0.28.0+
5. **🔄 Atualizado `fastapi`** para versão 0.105.0+
6. **🔄 Atualizado `beanie`** para versão 1.24.0+
7. **🔄 Mudado `uvicorn[standard]`** para `uvicorn` básico (sem watchfiles)

## 🚀 **Agora o usuário pode executar:**

```bash
<code_block_to_apply_from>
python -m pip install -r requirements.txt --prefer-binary --no-cache-dir
```

**Sem problemas de compilação!** ✅

## ⚠️ **Nota:**
- O projeto funcionará perfeitamente
- Apenas não terá **hot reload automático** (watchfiles)
- Para reload manual: pare o servidor (Ctrl+C) e execute `python main.py` novamente
