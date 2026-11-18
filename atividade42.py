print("--- CADASTRO DE SEGURANÇA DE BANCO CENTRAL---")

for tentativa in range(3):

    gerente = input("Digite seu o nome do gerente:  ").strip()
    cidade = input("Digite o nome da cidade: ").strip()
    cpf = input("Digite o seu cpf (Deve conter apenas numeros): ").strip()
    agencia = input("Digite sua agencia (Deve conter apenas numeros): ").strip()
    conta = input("Digite o numero da sua conta (Deve conter apenas numeros): ").strip()
    nivel = input("Digite o seu nivel (Deve ser DIRETOR) : ").strip().upper()
    senha = input("Digite sua senha (Deve pode ser 123) : ").strip()
    chave = input("Digite o numero da sua chave (Deve ser ALPHA) : ").strip().upper()

    if gerente.isalpha() and gerente.isalpha() and \
       cidade.isalpha() and \
       cpf.isdigit() and \
       agencia.isdigit() and \
       conta.isdigit() and \
       len(nivel) and nivel.isalpha() == "DIRETOR" and \
       len(senha) and senha.isdigit() != "123" and \
       len(chave) and chave.isalpha() == "ALPHA":

        print(f"Acesso liberado! Bem-vindo ao sistema, {gerente}.")
        break

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")