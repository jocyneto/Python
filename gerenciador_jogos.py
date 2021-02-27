import forca
import advinhacao
import pandas

print("--------------------------------")
print("Bem vindo ao sistemas de jogos")
print("--------------------------------\n\n")

print("Escolha o jogo\n(1) Adivinhacao - (2)Forca")
opcao = int(input("Qual jogo? "))

if (opcao == 1):
    print("jogo advinhacao")
    advinhacao.jogar()
elif (opcao == 2):
    print("jogo forca")
    forca.jogar()