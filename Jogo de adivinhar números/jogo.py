import random

play = True
sort = True

while play:
    if sort == True:
        number = random.randint(1, 10)
        sort = False
        print("Número sorteado! Tente adivinhar.")

    ideia = int(input("Digite um número entre 1 e 10: "))

    if ideia == number:
        print("\nParabéns! Você acertou o número!")
        replay = input("Deseja jogar novamente? (s/n): ").lower()
        if replay == 's':
            sort = True
        else:
            play = False
            print("Obrigado por jogar! Até a próxima.")

    elif ideia < number:
        print("\nErrado! o número que estou pensando é maior :( ")
    else:
        print("\nErrado! o número que estou pensando é menor :( ")   

