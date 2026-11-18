# O usuário digita o que quer fazer
objetivo = input("O que você quer postar? (fotos / videos / textos): ")

# O programa recomenda a rede social
if objetivo == "fotos":
    print("Recomendação: Instagram")
elif objetivo == "videos":
    print("Recomendação: TikTok ou YouTube")
elif objetivo == "noticias" or objetivo == "twitter":
    print("Recomendação: X (antigo Twitter) ou Threads")
else:
    print("Essa opção não esta no banco de dados.")