# Avaliação Full Stack - Encurtador de URL

Este projeto Full Stack foi desenvolvido para demonstrar habilidades no desenvolvimento de aplicações modernas, utilizando tecnologias de ponta para criar um sistema completo de encurtamento de URLs, desde o Front-End até o Back-End.

## 📌 Funcionalidades Implementadas

✅ **Encurtamento de URLs** com validação automática  
✅ **Redirecionamento inteligente** e rastreamento de cliques  
✅ **Métricas em tempo real** (última hora, dia e mês)  
✅ **Pesquisa avançada** por Short ID nas métricas  
✅ **Interface moderna** com tema escuro responsivo  
✅ **API documentada** com Swagger/OpenAPI  
✅ **Contabilização automática** de acessos sem refresh da página  

## 🛠 Tecnologias Utilizadas

### 🌐 Front-End:
- **React 18** - Biblioteca moderna para criação de interfaces dinâmicas
- **TypeScript** - Tipagem estática para maior robustez do código
- **Vite** - Build tool de alta performance para desenvolvimento
- **TailwindCSS** - Framework de estilização para design responsivo e elegante
- **CSS3 Customizado** - Estilização avançada com tema escuro e animações

### ⚙️ Back-End:
- **Python 3.11+** - Linguagem moderna e versátil
- **FastAPI** - Framework web de alta performance com validação automática
- **Beanie ODM** - Mapeamento objeto-documento moderno para MongoDB
- **Pydantic** - Validação robusta de dados e serialização
- **Motor** - Driver assíncrono para MongoDB com alta performance
- **Uvicorn** - Servidor ASGI de alta velocidade

### 🗄 Banco de Dados:
- **MongoDB Atlas** - Banco de dados NoSQL na nuvem, escalável e eficiente

## 🚀 Como Rodar o Projeto

### 📌 Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas no seu ambiente:

- **Python 3.11+**
- **Node.js** (versão recomendada: 18+)
- **NPM** ou **Yarn**
- **Git**

### 🎨 Como Rodar o Front-End

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/encurtador-url-fullstack.git
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

### 🔧 Como Rodar o Back-End

1. **Acesse a pasta do Back-End:**
   ```bash
   cd backend
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o MongoDB:**
   O projeto já vem configurado com um banco MongoDB Atlas de demonstração.  
   Nenhuma configuração adicional é necessária para execução.

5. **Execute a aplicação:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. **O servidor estará rodando em:**
   ```
   http://localhost:8000
   ```

7. **Acesse a documentação Swagger:**
   ```
   http://localhost:8000/docs
   ```

## 📊 Como Usar o Sistema

1. **Acesse a aplicação** em `http://localhost:5173`
2. **Cole uma URL longa** no campo de entrada
3. **Clique em "Encurtar URL"** para gerar o link encurtado
4. **Utilize as funcionalidades:**
   - **Copiar Link:** Copia a URL encurtada para área de transferência
   - **Abrir Link:** Abre a URL original e registra métrica automaticamente
   - **Pesquisar:** Use o campo de busca para filtrar métricas por Short ID
5. **Visualize métricas** em tempo real na tabela de estatísticas

## 🔗 Endpoints da API

### Principais Rotas Disponíveis:

- `POST /api/urls` - Criar nova URL encurtada
- `GET /api/urls` - Listar todas as URLs cadastradas  
- `GET /api/metrics` - Obter métricas de acessos
- `POST /api/metrics/{short_id}` - Registrar novo acesso
- `GET /{short_id}` - Redirecionamento para URL original

### 📖 Documentação Completa:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## 💡 Destaques Técnicos

🎯 **Arquitetura Moderna:** Separação clara entre frontend e backend  
⚡ **Performance:** Uso de tecnologias assíncronas e otimizadas  
🔒 **Validação:** Validação robusta de dados em todas as camadas  
📱 **Responsividade:** Interface adaptável para todos os dispositivos  
🎨 **UX/UI:** Design moderno com feedback visual e animações  
📊 **Métricas:** Sistema completo de analytics em tempo real  

## 📜 Autor

👤 **[Seu Nome]**  
📧 **Email:** [seu.email@exemplo.com]  
🔗 **LinkedIn:** [https://www.linkedin.com/in/seu-perfil/]  
🐙 **GitHub:** [https://github.com/seu-usuario]  

---

🚀 **Projeto desenvolvido como parte de um desafio Full Stack, demonstrando proficiência em tecnologias modernas de desenvolvimento web.**
