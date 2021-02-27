import random


def jogar():
    print("--------------------------------")
    print("Bem vindo ao jogo de ADVINHACAO")
    print("--------------------------------\n\n")

    # numero_secreto = round(random.uniform(1,20))
    numero_secreto = random.randrange(1, 21)
    print(numero_secreto)
    total_de_chutes = 0
    pontos = 1000

    print("Escolha o nivel do jogo: \n(1) Fácil - (2) Médio - (3)Difícil")
    nivel = int(input("Digite a escolha: "))

    if (nivel == 1):
        total_de_chutes = 15
    elif (nivel == 2):
        total_de_chutes = 10
    else:
        total_de_chutes = 5

    for rodada in range(1, total_de_chutes + 1):
        print(f"\nRoda {rodada} de {total_de_chutes}")

        chute_str = input("Digite o chute: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 20):
            print("\nDigite um número de 1 a 20, tente novamente!!!")
            continue  # continua o laço, porém pula para proxima interação

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou! E fez {pontos:04} pontos!")
            break
        else:
            if (maior):
                print("Errou! Seu chute foi maior que o numero secreto")
            elif (menor):
                print("Errou! Seu chute foi menor que o numero secreto")
        pontos_perdidos = abs(chute - numero_secreto)
        pontos -= pontos_perdidos

    print("Game over!")