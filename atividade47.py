print("---Registro de Software em Blockchain---")

for tentativa in range(3):
    app = input("Digite o app:").strip()
    Dev = input("Digite o dev:").strip()
    Email = input("Digite o seu email:").strip()
    Versao = input("Digite a versao:").strip()
    hash = input("10 carac:").strip()
    Token = input("Digite o seu Token, nao pode ser Lixo:").strip()
    Contrato = input("5 num:").strip()
    Rede = input("Digite a sua rede:").strip().upper()
    Bloco = input("Digite o seu Bloco").strip()
    Minerador = input("Digiete o minerador").strip()
    Taxa = input("Digite a sua taxa").strip()
    Chave = input("Digite a sua chave").strip()
    Wallet = input("Digige o wallet").strip()

    if app.isalpha() and app.isalpha() and \
       Dev.isalpha() and \
       Contrato.isdigit() and \
       Bloco.isdigit() and \
       len(Rede) and Rede.isalpha() == "ETHEREUM" and \
       len(Token) and Token.isalpha() == "Lixo":
    
     print(f"Acesso liberado! Bem-vindo ao sistema, {app}.")
    break
else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")