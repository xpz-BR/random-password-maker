# 🔒 Gerador de Senhas Seguras (CSPRNG)

## Sobre o Projeto
Script em Python desenvolvido para a geração de credenciais fortes e imprevisíveis, utilizando geradores de números pseudoaleatórios criptograficamente seguros (CSPRNG). 

Projetado originalmente como prática de **Lógica de Programação** e evoluído com foco em **Blue Team / Cibersegurança** na **XPZ Company**.

## Funcionalidades
- **Aleatoriedade Segura:** Uso do módulo `secrets` integrado ao CSPRNG do sistema operacional.
- **Variedade de Caracteres:** Combinação automática de letras (maiúsculas e minúsculas), números e símbolos (`string`).
- **Validação de Tamanho:** Regra de comprimento mínimo (pelo menos 8 caracteres) para prevenção de senhas fracas.
- **Tratamento de Exceções:** Validação de entradas no terminal para prevenir falhas de execução.

## Tecnologias Utilizadas
- **Python 3**
- `secrets` — Geração criptograficamente segura de escolhas aleatórias.
- `string` — Conjuntos pré-definidos de caracteres ASCII.

## Como Executar
1. Certifique-se de ter o Python 3 instalado.
2. Baixe o arquivo `password_generator.py`.
3. Execute no terminal:
   ```bash
   py password_generator.py