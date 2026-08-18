import secrets
import string

secrets.randbelow(10)

def gerar_senha(comprimento):

    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    if comprimento < 8:
        print("O comprimento deve ser de pelo menos 8 caracteres.")
        return None
    
    senha = ''.join(secrets.choice(caracteres) for i in range(comprimento))
    
    return senha

comprimento_desejado = int(input("Digite o número de caracteres desejado para a senha: "))
senha_gerada = gerar_senha(comprimento_desejado)
print(f"Esta é sua senha gerada: {senha_gerada}")