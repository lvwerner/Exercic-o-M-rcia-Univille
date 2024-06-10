import os
import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Obter o diretório do arquivo atual
diretorio = os.path.dirname(os.path.abspath(_file_))

# Buscar músicas na pasta atual
print("Buscando músicas...")
musicas = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith(".mp3")]

if not musicas:
    print("Nenhuma música encontrada.")
else:
    print("Músicas encontradas:")
    for i, musica in enumerate(musicas):
        print(f"{i+1}. {musica}")

    escolha = input("Digite o número da música que deseja reproduzir: ")
    while not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(musicas):
        print("Escolha inválida.")
        escolha = input("Digite o número da música que deseja reproduzir: ")

    # Carregar o arquivo de áudio escolhido
    caminho_musica = os.path.join(diretorio, musicas[int(escolha) - 1])
    pygame.mixer.music.load(caminho_musica)

    # Reproduzir a música
    pygame.mixer.music.play()

    # Loop para interação com o usuário
    while True:
        opcao = input("Digite 'p' para pausar, 'r' para retomar, 'n' para próxima música ou 's' para sair: ")

        if opcao == 'p':
            pygame.mixer.music.pause()
        elif opcao == 'r':
            pygame.mixer.music.unpause()
        elif opcao == 'n':
            # Passar para a próxima música
            escolha = (int(escolha) % len(musicas)) + 1
            caminho_musica = os.path.join(diretorio, musicas[escolha - 1])
            pygame.mixer.music.load(caminho_musica)
            pygame.mixer.music.play()
            print(f"Reproduzindo próxima música: {musicas[escolha - 1]}")
        elif opcao == 's':
            pygame.mixer.music.stop()
            break
        else:
            print("Opção inválida. Por favor, digite 'p', 'r', 'n' ou 's'.")