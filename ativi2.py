print ("--------------------------------BANCO DIGITAL-----------------------------------------")

for tentativas in range(5):
    nome_cliente = input("Digite o nome do cliente: ").strip()
    nome_moeda = input("Digite o nome da ciptomoeda: ").strip()
    cod_hash = input("Digite o codigo hash da carteira: ").strip().upper()
    data = input("Digite a data da transação: ").strip()
    id = input("Digite o id numerico do bloco: ").strip()
    email = input("Digite o email de suporte: ").strip().lower()
    quantidade = input("Digite a quantidade de moedas: ").strip()
    cod_taxa = input("Digite o codigo da taxa: ").strip().upper()
    pais = input("Digite o pais da corretora: ").strip()
    status = input("Digite o status: ").strip().upper

    if nome_cliente.isalpha() and \
    nome_moeda.isdigit() and \
    cod_hash.isalnum() and \
    id.isdigit() and \
    pais.isalpha() and \
    quantidade.isdigit() and \
    cod_taxa.isdigit() and \
     email.count ("@") == 1 and email.endswith (".com"):
            data.count ("/") == 2 and \
            status == "APROVADO" and \
            print(f"\nSUCESSO: Astronauta {nome_cliente}, foguete {nome_cliente} liberado!")
            break
    else:
           print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")
           print("-" * 40)
else:
       print("Acesso negado")