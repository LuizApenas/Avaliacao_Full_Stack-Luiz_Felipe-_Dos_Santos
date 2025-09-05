@echo off
chcp 65001 >nul
echo 🚀 Iniciando instalacao das dependencias do backend em etapas...
echo ⏱️  Este processo pode demorar alguns minutos...
echo.

REM Verificar se requirements.txt existe
if not exist requirements.txt (
    echo ❌ Arquivo requirements.txt nao encontrado!
    echo Certifique-se de estar no diretorio backend do projeto.
    pause
    exit /b 1
)

REM Preparacao do ambiente
echo ============================================================
echo 🔧 PREPARACAO DO AMBIENTE
echo ============================================================

echo 🔄 Atualizando pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo ⚠️  Falha ao atualizar pip, continuando...
)

echo 🔄 Instalando setuptools e wheel...
python -m pip install --upgrade setuptools wheel
if errorlevel 1 (
    echo ⚠️  Falha ao instalar setuptools/wheel, continuando...
)

REM ETAPA 1: Dependencias base
echo.
echo ============================================================
echo 📦 ETAPA 1: Dependencias base do sistema
echo ============================================================
python -m pip install "certifi>=2024.0.0" --prefer-binary --no-cache-dir
python -m pip install "idna>=3.4,<4.0" --prefer-binary --no-cache-dir
python -m pip install "sniffio>=1.3.0,<2.0.0" --prefer-binary --no-cache-dir
python -m pip install "click>=8.1.0,<9.0.0" --prefer-binary --no-cache-dir
python -m pip install "colorama>=0.4.6,<0.5.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 1 - Concluida!
timeout /t 2 /nobreak >nul

REM ETAPA 2: Tipos e extensoes
echo.
echo ============================================================
echo 📦 ETAPA 2: Tipos e extensoes fundamentais
echo ============================================================
python -m pip install "typing-extensions>=4.8.0,<5.0.0" --prefer-binary --no-cache-dir
python -m pip install "annotated-types>=0.6.0,<0.8.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 2 - Concluida!
timeout /t 2 /nobreak >nul

REM ETAPA 3: Utilitarios core
echo.
echo ============================================================
echo 📦 ETAPA 3: Utilitarios core
echo ============================================================
python -m pip install "python-dotenv>=1.0.0,<1.1.0" --prefer-binary --no-cache-dir
python -m pip install "anyio>=4.0.0,<5.0.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 3 - Concluida!
timeout /t 2 /nobreak >nul

REM ETAPA 4: HTTP core
echo.
echo ============================================================
echo 📦 ETAPA 4: HTTP core
echo ============================================================
python -m pip install "h11>=0.14.0,<0.15.0" --prefer-binary --no-cache-dir
python -m pip install "httpcore>=1.0.0,<2.0.0" --prefer-binary --no-cache-dir
python -m pip install "httpx>=0.25.0,<0.27.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 4 - Concluida!
timeout /t 2 /nobreak >nul

REM ETAPA 5: Validacao (Pydantic)
echo.
echo ============================================================
echo 📦 ETAPA 5: Validacao (Pydantic)
echo ============================================================
python -m pip install "pydantic>=2.5.0,<3.0.0" --prefer-binary --no-cache-dir
python -m pip install "pydantic-settings>=2.1.0,<3.0.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 5 - Concluida!
timeout /t 2 /nobreak >nul

REM ETAPA 6: Web framework base
echo.
echo ============================================================
echo 📦 ETAPA 6: Web framework base
echo ============================================================
python -m pip install "starlette>=0.27.0,<0.29.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 6 - Concluida!
timeout /t 2 /nobreak >nul

REM ETAPA 7: FastAPI
echo.
echo ============================================================
echo 📦 ETAPA 7: FastAPI
echo ============================================================
python -m pip install "fastapi>=0.104.1,<0.106.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 7 - Concluida!
timeout /t 2 /nobreak >nul

REM ETAPA 8: Servidor ASGI
echo.
echo ============================================================
echo 📦 ETAPA 8: Servidor ASGI
echo ============================================================
python -m pip install "httptools>=0.6.0,<0.7.0" --prefer-binary --no-cache-dir
python -m pip install "python-multipart>=0.0.6,<0.1.0" --prefer-binary --no-cache-dir
python -m pip install "watchfiles>=0.21.0,<0.23.0" --prefer-binary --no-cache-dir
python -m pip install "websockets>=12.0,<14.0" --prefer-binary --no-cache-dir
python -m pip install "uvicorn[standard]>=0.24.0,<0.26.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 8 - Concluida!
timeout /t 2 /nobreak >nul

REM ETAPA 9: MongoDB
echo.
echo ============================================================
echo 📦 ETAPA 9: MongoDB
echo ============================================================
python -m pip install "pymongo>=4.6.0,<5.0.0" --prefer-binary --no-cache-dir
python -m pip install "motor>=3.3.0,<4.0.0" --prefer-binary --no-cache-dir
python -m pip install "beanie>=1.23.0,<2.0.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 9 - Concluida!
timeout /t 2 /nobreak >nul

REM ETAPA 10: Testes
echo.
echo ============================================================
echo 📦 ETAPA 10: Testes
echo ============================================================
python -m pip install "pytest>=7.4.0,<8.0.0" --prefer-binary --no-cache-dir
python -m pip install "pytest-asyncio>=0.21.0,<0.23.0" --prefer-binary --no-cache-dir
echo ✅ ETAPA 10 - Concluida!

echo.
echo ============================================================
echo 🎉 INSTALACAO CONCLUIDA COM SUCESSO!
echo ============================================================
echo.
echo Para iniciar o servidor, execute:
echo   python main.py
echo ou
echo   uvicorn main:app --reload --host 0.0.0.0 --port 8000
echo.
echo Para verificar se tudo esta funcionando:
echo   python -c "import fastapi, uvicorn, motor, beanie; print('✅ Todas as dependencias principais importadas com sucesso!')"
echo.
pause
