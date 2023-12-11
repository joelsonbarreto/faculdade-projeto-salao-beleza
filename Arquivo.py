import pickle

def salvar_em_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(dados, arquivo)

def carregar_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return []
