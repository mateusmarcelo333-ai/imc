print ("--------------------------------Servidor de dados-----------------------------------------")

for tentativas in range(5):
    Nome_do_administrador = input("Digite o nome do Administrador: ").strip()
    Cargo_do_Usuario = input("Digite o nome do cargo de usuario: ").strip()
    codigo_Do_Sevidor = input("Digite o codigo do servidor: ").strip().upper()
    ip_do_terminal = input("Digite o ip do terminal: ").strip()
    Porta_de_Rede= input("Digite a porta de rede: ").strip()
    Setor_Responsavel = input("Digite o seu setor responsavel: ").strip().lower()
    Protocolo_do_servidor = input("Digite o protocolo do servidor: ").strip()
    Senha_provisoria = input("Digite a senha provisoria: ").strip().upper()
    Dominio_Corporativo = input("Digite o seu Dominio Corporativo: ").strip()
    Confirmaçao_de_segurança = input("Digite a confirmaçao: ").strip().upper()

    if codigo_Do_Sevidor.isalnum() and \
       Protocolo_do_servidor.isalnum() and \
       Porta_de_Rede.isdigit() and \
       ip_do_terminal.isdigit() and \
       Cargo_do_Usuario.isalpha() and \
       Setor_Responsavel.isalpha() and \
       Dominio_Corporativo.endswith ("org") and \
       len(Senha_provisoria) == 8 and\
       Confirmaçao_de_segurança == "LIBERADO":
       
       print(f"\nSUCESSO:  {Nome_do_administrador},  {Cargo_do_Usuario} liberado!")
       break
    else:
                  print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")
                  print("-" * 40)
else:
              print("Acesso negado")