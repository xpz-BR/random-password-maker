import random
import string

def gerar_senha(comprimento):
    # Docstring: explica o que a função faz
    """
    Gera uma senha aleatória com base no comprimento especificado, 
    incluindo letras, números e símbolos.
    """
    
    # Conjunto de todos os caracteres possíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Validação de segurança mínima
    if comprimento < 4:
        print("O comprimento deve ser de pelo menos 4 caracteres.")
        return None
    
    # Usa o 'join' com 'random.choice' para fazer a senha
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    
    return senha

if __name__ == "__main__":
    
    print("--- Gerador de Senhas Simples ---")
    
    while True:
        try:
            comprimento_desejado = int(input("Digite o comprimento desejado para a senha (ex: 12): "))
            
            senha_gerada = gerar_senha(comprimento_desejado)
            
            if senha_gerada:
                print(f"\nSua senha gerada é: {senha_gerada}")
                break 
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
        except Exception as e:
            # Pega qualquer outro erro inesperado
            print(f"Ocorreu um erro: {e}")