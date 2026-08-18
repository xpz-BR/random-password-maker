import secrets
import string


def gerar_senha(comprimento: int) -> str | None:
    if comprimento < 8:
        print("O comprimento deve ser de pelo menos 8 caracteres.")
        return None

    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(caracteres) for _ in range(comprimento))


try:
    comprimento_desejado = int(input("Digite o número de caracteres para a senha: "))
    senha_gerada = gerar_senha(comprimento_desejado)

    if senha_gerada:
        print(f"Esta é sua senha gerada: {senha_gerada}")
except ValueError:
        print("Erro: digite apenas números inteiros.")