print("--- SISTEMA DE RASTREAMENTO DE SATÉLITES ---")

for tentativa in range(5):
# 1. ENTRADA E TRATAMENTO DOS DADOS
 satelite = input("Nome do Satélite: ").strip().upper()
 agencia = input("Sigla da Agência: ").strip().upper()
 operador = input("Operador Responsável: ").strip().title()
 cidade = input("Cidade da Estação: ").strip().title()
 telemetria = input("Código de Telemetria: ").strip()
 chave = input("Chave Criptográfica (Ex: SAT-99): ").strip()
 freq = input("Frequência em MHz: ").strip()
 altitude = input("Altitude Orbital: ").strip()
 data = input("Data do Apogeu (DD-MM-AAAA): ").strip()
 email = input("E-mail da Defesa: ").strip().lower()
 senha = input("Senha de Acesso (Mínimo 8 dígitos): ").strip()
 autorizacao = input("Autorização de Órbita (CONFIRMADO): ").strip().upper()
# 2. TRATAMENTO DA DATA COM .replace()
 data_formatada = data.replace("-", "/")
# 3. VALIDAÇÃO DIRETA COM IF + AND + QUEBRA DE LINHA (\)
 if operador.isalpha() and \
 cidade.isalpha() and \
 telemetria.isalnum() and \
 chave.isalnum() and \
 chave.startswith("SAT-") and \
 freq.isdigit() and \
    altitude.isdigit() and \
    data_formatada.count("/") == 2 and \
    len(data_formatada) == 10 and \
    email.endswith(".defesa.mil.br") and \
    len(senha) >= 8 and \
    autorizacao == "CONFIRMADO":
# 4. MÁSCARA DE PROTEÇÃO DE SENHA
    senha_oculta = "*" * len(senha)
    print(f"\nSUCESSO: Satélite {satelite} ({agencia}) rastreado por {operador} em {cidade}!")
    print(f"Data Padronizada: {data_formatada} | Senha Protegida: {senha_oculta}")
    break
 else:
    print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
    print("-" * 40)
else:
 print("\nBLOQUEADO: 5 tentativas esgotadas. Notifique o Comando Espacial.")