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
