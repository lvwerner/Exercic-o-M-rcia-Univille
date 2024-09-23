import numpy as np
import random

# Inicializa os setores do estacionamento
setor_A = np.full(5, None)
setor_B = np.full(5, None)
setor_C = np.full(5, None)

# Dicionário para armazenar o status dos veículos
veiculos = {}

def escolher_setor(setor=None):
    """
    Retorna o setor escolhido ou um setor aleatório se nenhum for fornecido.
    :param setor: Letra do setor (A, B ou C) ou None para escolha aleatória.
    :return: Setor e o array correspondente.
    """
    if setor is None:
        setor = random.choice(['A', 'B', 'C'])  # Escolhe aleatoriamente A, B ou C
    if setor == 'A':
        return 'A', setor_A
    elif setor == 'B':
        return 'B', setor_B
    elif setor == 'C':
        return 'C', setor_C
    return None, None

def ocupar_vaga(placa, setor=None):
    """
    Ocupa uma vaga no estacionamento. O setor pode ser especificado ou aleatório.
    :param placa: Placa do veículo.
    :param setor: Setor onde o veículo deseja estacionar (A, B, ou C). Se None, escolher aleatoriamente.
    :return: Mensagem de sucesso ou erro.
    """
    if placa in veiculos:
        return "Veículo já está estacionado."

    # Escolhe setor (pode ser específico ou aleatório)
    setor, vagas = escolher_setor(setor)

    if vagas is None:
        return "Setor inválido."

    # Verifica se há vagas disponíveis no setor escolhido
    vagas_livres = [i for i, v in enumerate(vagas) if v is None]
    if not vagas_livres:
        return f"Não há vagas disponíveis no setor {setor}."

    # Escolhe uma vaga aleatoriamente entre as disponíveis
    vaga_escolhida = random.choice(vagas_livres)
    vagas[vaga_escolhida] = placa
    veiculos[placa] = setor
    return f"Veículo com placa {placa} estacionado na vaga {vaga_escolhida} do setor {setor}."

def liberar_vaga(placa):
    """
    Libera a vaga do estacionamento.
    :param placa: Placa do veículo.
    :return: Mensagem de sucesso ou erro.
    """
    if placa not in veiculos:
        return "Veículo não está estacionado."

    setor = veiculos.pop(placa)
    if setor == 'A':
        vagas = setor_A
    elif setor == 'B':
        vagas = setor_B
    elif setor == 'C':
        vagas = setor_C

    vaga_ocupada = np.where(vagas == placa)[0][0]
    vagas[vaga_ocupada] = None
    return f"Veículo com placa {placa} retirado da vaga {vaga_ocupada} do setor {setor}."

def exibir_vagas_disponiveis():
    """
    Exibe as vagas disponíveis no estacionamento por setor.
    """
    def vagas_disponiveis(setor):
        vagas = setor_A if setor == 'A' else setor_B if setor == 'B' else setor_C
        vagas_livres = [i for i, v in enumerate(vagas) if v is None]
        return vagas_livres

    print("Vagas disponíveis por setor:")
    for setor in ['A', 'B', 'C']:
        vagas = vagas_disponiveis(setor)
        print(f"Setor {setor}: {vagas if vagas else 'Nenhuma vaga disponível'}")

def consultar_veiculo(placa):
    """
    Consulta o setor onde o veículo está estacionado.
    :param placa: Placa do veículo.
    :return: Setor onde o veículo está ou mensagem de erro.
    """
    if placa not in veiculos:
        return "Veículo não está estacionado."

    return f"Veículo com placa {placa} está no setor {veiculos[placa]}."

def menu():
    """
    Exibe o menu e solicita ao usuário que escolha uma opção.
    """
    while True:
        print("\n--- Menu Estacionamento ---")
        print("1. Estacionar veículo")
        print("2. Consultar veículo pela placa")
        print("3. Liberar veículo")
        print("4. Exibir vagas disponíveis")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            placa = input("Digite a placa do veículo: ").upper()
            setor = input("Digite o setor (A, B, C ou deixe vazio para aleatório): ").upper() or None
            print(ocupar_vaga(placa, setor))

        elif opcao == '2':
            placa = input("Digite a placa do veículo para consulta: ").upper()
            print(consultar_veiculo(placa))

        elif opcao == '3':
            placa = input("Digite a placa do veículo para liberar a vaga: ").upper()
            print(liberar_vaga(placa))

        elif opcao == '4':
            exibir_vagas_disponiveis()

        elif opcao == '5':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu interativo
if __name__ == "__main__":
    menu()
