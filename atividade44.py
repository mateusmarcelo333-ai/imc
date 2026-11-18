print("---Sturp---")

for tentativa in range(3):

    nomedaStarptup = input("Digite seu nome:").strip()
    Email = input("Digite seu E-mail:").strip()
    Setor = input("Digite o seu setor:").strip()
    Anodefundaçao = input("Digite o seu Ano de fundaçao:").strip()
    CNPJ = input("14 num:").strip()
    investimento = input("Digite o seu investimento:").strip()
    Moeda = input("USD").strip().upper()
    sede = input("Digite a sua sede:").strip().upper()
    funcionarios = input("Digite seu nome de funcionario:").strip()
    site = input("Digite o link do site:").strip()
    Linguagem = input("Digite a linguagem:").strip()
    Versao = input("Digite a sua versao:").strip()

    if nomedaStarptup.isalpha() and nomedaStarptup.isalpha() and \
       Email.isalpha() and \
       Setor.isalpha() and \
       Anodefundaçao.isalpha() and \
       CNPJ.isdigit() and \
       investimento.isdigit() and \
       len(Moeda) and Moeda.isalpha() == "USD" and \
       len(sede) and sede.isalpha() == "Aceito":
       
        print(f"Acesso liberado! Bem-vindo ao sistema, {nomedaStarptup}.")
        break
else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")