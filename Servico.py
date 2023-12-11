import datetime
from Arquivo import carregar_do_arquivo, salvar_em_arquivo


class Servico:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f"Descrição: {self.descricao}\nPreço: {self.preco}\n"

    def cadastrar_servico():
        descricao = input("Informe a descrição do serviço: ")
        preco = float(input("Informe o preço do serviço: "))

        servicos = carregar_do_arquivo("servicos.txt")
    
        novo_servico = Servico(descricao, preco)
        servicos.append(novo_servico)
        salvar_em_arquivo(servicos, "servicos.txt")
        print("Serviço cadastrado com sucesso!")

    
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
        
    def agendar_servico(cliente, servico):
        data = input("Informe a data do agendamento (formato dd/mm/yyyy): ")
        
        try:
            data_agendamento = datetime.datetime.strptime(data, "%d/%m/%Y").date()
            data_atual = datetime.date.today()

            if data_agendamento < data_atual:
                print("Não é possível agendar para uma data anterior à data atual.")
                return

            print(f"Serviço agendado para {data_agendamento}")
        except ValueError:
            print("Formato de data inválido. Use o formato dd/mm/yyyy.") 