def escolher_servico(servicos):
    print("Serviços disponíveis:")
    for i, servico in enumerate(servicos, 1):
        print(f"{i} - {servico.descricao}")

    indice_servico = int(input("Escolha o serviço (pelo número): "))

    if 1 <= indice_servico <= len(servicos):
        return servicos[indice_servico - 1]
    else:
        print("Índice de serviço inválido.")
        return None