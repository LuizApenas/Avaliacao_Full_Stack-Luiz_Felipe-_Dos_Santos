#!/usr/bin/env python3
"""
Script para instalar dependências do projeto em etapas ordenadas.
Este script evita conflitos de dependências instalando em ordem específica.
"""

import subprocess
import sys
import os
import time

def run_command(command, description):
    """Executa um comando e mostra o resultado."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Erro:")
        print(f"Código de saída: {e.returncode}")
        print(f"Erro: {e.stderr}")
        return False

def install_packages_in_stages():
    """Instala pacotes em etapas ordenadas para evitar conflitos."""
    
    # Definir etapas de instalação
    stages = [
        {
            "name": "ETAPA 1: Dependências base do sistema",
            "packages": [
                "certifi>=2024.0.0",
                "idna>=3.4,<4.0",
                "sniffio>=1.3.0,<2.0.0",
                "click>=8.1.0,<9.0.0",
                "colorama>=0.4.6,<0.5.0"
            ]
        },
        {
            "name": "ETAPA 2: Tipos e extensões fundamentais",
            "packages": [
                "typing-extensions>=4.8.0,<5.0.0",
                "annotated-types>=0.6.0,<0.8.0"
            ]
        },
        {
            "name": "ETAPA 3: Utilitários core",
            "packages": [
                "python-dotenv>=1.0.0,<1.1.0",
                "anyio>=4.0.0,<5.0.0"
            ]
        },
        {
            "name": "ETAPA 4: HTTP core",
            "packages": [
                "h11>=0.14.0,<0.15.0",
                "httpcore>=1.0.0,<2.0.0",
                "httpx>=0.25.0,<0.27.0"
            ]
        },
        {
            "name": "ETAPA 5: Validação (Pydantic)",
            "packages": [
                "pydantic>=2.5.0,<3.0.0",
                "pydantic-settings>=2.1.0,<3.0.0"
            ]
        },
        {
            "name": "ETAPA 6: Web framework base",
            "packages": [
                "starlette>=0.27.0,<0.29.0"
            ]
        },
        {
            "name": "ETAPA 7: FastAPI",
            "packages": [
                "fastapi>=0.104.1,<0.106.0"
            ]
        },
        {
            "name": "ETAPA 8: Servidor ASGI",
            "packages": [
                "httptools>=0.6.0,<0.7.0",
                "python-multipart>=0.0.6,<0.1.0",
                "watchfiles>=0.21.0,<0.23.0",
                "websockets>=12.0,<14.0",
                "uvicorn[standard]>=0.24.0,<0.26.0"
            ]
        },
        {
            "name": "ETAPA 9: MongoDB",
            "packages": [
                "pymongo>=4.6.0,<5.0.0",
                "motor>=3.3.0,<4.0.0",
                "beanie>=1.23.0,<2.0.0"
            ]
        },
        {
            "name": "ETAPA 10: Testes",
            "packages": [
                "pytest>=7.4.0,<8.0.0",
                "pytest-asyncio>=0.21.0,<0.23.0"
            ]
        }
    ]
    
    # Executar cada etapa
    for stage in stages:
        print(f"\n{'='*60}")
        print(f"📦 {stage['name']}")
        print(f"{'='*60}")
        
        for package in stage['packages']:
            install_cmd = f"{sys.executable} -m pip install '{package}' --prefer-binary --no-cache-dir"
            if not run_command(install_cmd, f"Instalando {package}"):
                print(f"⚠️  Falha ao instalar {package}, continuando...")
                time.sleep(1)
        
        print(f"✅ {stage['name']} - Concluída!")
        time.sleep(2)  # Pausa entre etapas
    
    return True

def main():
    """Função principal para instalação das dependências."""
    print("🚀 Iniciando instalação das dependências do backend em etapas...")
    print("⏱️  Este processo pode demorar alguns minutos...")
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("requirements.txt"):
        print("❌ Arquivo requirements.txt não encontrado!")
        print("Certifique-se de estar no diretório backend do projeto.")
        sys.exit(1)
    
    # Atualizar pip primeiro
    print("\n" + "="*60)
    print("🔧 PREPARAÇÃO DO AMBIENTE")
    print("="*60)
    
    if not run_command(f"{sys.executable} -m pip install --upgrade pip", "Atualizando pip"):
        print("⚠️  Falha ao atualizar pip, continuando...")
    
    # Instalar setuptools e wheel
    if not run_command(f"{sys.executable} -m pip install --upgrade setuptools wheel", "Instalando setuptools e wheel"):
        print("⚠️  Falha ao instalar setuptools/wheel, continuando...")
    
    # Instalar dependências em etapas
    if install_packages_in_stages():
        print("\n" + "="*60)
        print("🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
        print("="*60)
        print("\nPara iniciar o servidor, execute:")
        print("  python main.py")
        print("ou")
        print("  uvicorn main:app --reload --host 0.0.0.0 --port 8000")
        print("\nPara verificar se tudo está funcionando:")
        print("  python -c \"import fastapi, uvicorn, motor, beanie; print('✅ Todas as dependências principais importadas com sucesso!')\"")
    else:
        print("\n❌ Falha na instalação das dependências.")
        print("\nTente executar o comando tradicional:")
        print(f"  {sys.executable} -m pip install -r requirements.txt --prefer-binary")
        sys.exit(1)

if __name__ == "__main__":
    main()
