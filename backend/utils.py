import string
import secrets

# Alfabeto: letras maiúsculas, minúsculas e dígitos
ALPHABET = string.ascii_letters + string.digits

def generate_short_id(length: int = 6) -> str:
    """Função que gera um ID de até 6 caracteres aleatórios, 
    biblioteca secrets do Python inves de randon por ser mais seguro"""
    if length <= 0:
        raise ValueError("O comprimento do ID encurtado deve ser maior que 0")

    return "".join(secrets.choice(ALPHABET) for _ in range(length))

def is_valid_short_id(value: str, length: int = 6) -> bool:
    """Função que valida as regras de criação de ID encurtado"""
    return len(value) == length and all(c in ALPHABET for c in value)