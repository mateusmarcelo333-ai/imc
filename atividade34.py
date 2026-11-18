for tentativa in range(3):
    
    passageiro = input("Nome do Passageiro: ").strip()
    destino = input("Destino: ").strip()
    passaporte = input("Passaporte (8 números): ").strip()
    voo = input("Voo (4 caracteres): ").strip()
    portao = input("Portão (Ex: A1): ").strip()
    assento = input("Assento (Ex: 12A): ").strip()
    if len(passageiro) > 3 and \
       destino.isalpha() and \
       len(passaporte) == 8 and passaporte.isdigit() and \
       len(voo) == 4 and \
       portao == "A1" and \
       len(assento) > 1:
        
        print("\nEmbarque validado! Emitindo cartão...")
        break
    else:
        print(f"\nErro nos dados. Você ainda tem {2 - tentativa} tentativa(s).")
        print("-" * 30)
else:
    print("\nTotem travado. Por favor, dirija-se ao balcão presencial.")
