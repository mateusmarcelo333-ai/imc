for tentativa in range(3):
    
    print(f"\n--- Reserva de Veículo (Tentativa {tentativa + 1}/3) ---")
    cliente = input("Nome do Cliente: ").strip()
    veiculo = input("Modelo do Veículo (ex: SEDAN): ").strip()
    cor = input("Cor do Veículo: ").strip()
    cnh = input("CNH (9 caracteres): ").strip()
    dias = input("Quantidade de dias: ").strip()
    seguro = input("Tipo de Seguro: ").strip()
    if veiculo.upper() == "SEDAN" and \
       cor.isalpha() and \
       len(cnh) == 9 and \
       dias.isdigit():
        
        print("\nSucesso: Reserva de Veículo de Luxo concluída!")
        break
    else:
        print("\nErro: Verifique se o veículo é SEDAN, se a cor não tem números e se a CNH tem 9 dígitos.")
        print("-" * 40)
else:
    print("\nERRO FATAL: Limite de tentativas excedido. Sistema de reservas bloqueado.")