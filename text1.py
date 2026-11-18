# o usuario  informa que tipo  de cliene le é:
tipo_cliente = input("Digite seu perfil (1: Estudutante / 2: idoso / 3: Publico comum): ")

if tipo_cliente == "1":
    print("Voce tem direito a 50% de desconto (Meia Estudante).")
elif tipo_cliente == "2":

    print("Voce tem direito a 50% de desconto (Meai Entrada idoso).")
else:
    print("voce pegara o valor de entrada inteira.")

    #o elif é a alternativa especifica: não é estudando?
    #Mas é idoso?

    #se não caiu nas regras de desconto acima, cal no else
    #automaticamente

    #Dois sinais de igual (==) é uma pergunta, diferente do = que guarda um valor
    ## o == compara os valores