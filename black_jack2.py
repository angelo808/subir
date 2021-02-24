import random

def bj():
    black_jack = 21
    mano = []
    mano_dealer = []
    baraja = ["As",2,3,4,5,6,7,8,9,10,"J","Q","K"] 

    for i in range(2):
        random.shuffle(baraja)
        mano.append(baraja[random.randint(0,12)])
        random.shuffle(baraja)
        mano_dealer.append(baraja[random.randint(0,12)])

    print("Tu baraja: ")
    print(mano[0], end=" ")
    print(mano[1])
    print("------------------")
    print("Baraja del crupier: ")
    print(mano_dealer[0], end=" ")
    print("??")

    for j in range(i+1):
        mano[j] = valor_carta(mano[j],1)
        mano_dealer[j] = valor_carta(mano_dealer[j],0)

    total = mano[0] + mano[1]
    total_dealer = mano_dealer[0]+mano_dealer[1]

    print("------------------")
    print("¿deseas mantener tu baraja?")
    print("a) Agregar una carta")
    print("b) Mantener ")
    op =input()

    if op == "a":
        while op == "a":   
            
            random.shuffle(baraja)
            mano.append(baraja[random.randint(0,12)])
            print("Carta agregada:",end=" ")
            print(mano[len(mano)-1])
            mano[len(mano)-1] = valor_carta(mano[len(mano)-1],1)
            print("------------------")
            total = total + mano[len(mano)-1]

            if total > black_jack:
                print("Perdiste, sobrepasaste el límite")
                carta_dealer(mano_dealer[1])
                game_over()
                
            else:
                print("¿desea agregar otra carta?")
                print("a) Sí")
                print("b) No")
                op = input()
    else:
        print("------------------")
        if total < total_dealer:
            print("Perdiste")
            carta_dealer(mano_dealer[1])
            game_over()

        if black_jack > total_dealer:
            random.shuffle(baraja)
            mano_dealer.append(baraja[random.randint(0,12)])
            print("Turno del cruiper.")
            carta_dealer(mano_dealer[1])
            print("Carta agregada:",end=" ")
            print(mano_dealer[len(mano_dealer)-1])
            mano_dealer[len(mano_dealer)-1] = valor_carta(mano_dealer[len(mano_dealer)-1],0)
            print("------------------")
            total_dealer = total_dealer + mano_dealer[len(mano_dealer)-1]

            if total_dealer > black_jack:
                print("El cruiper sobrepasó el límite.")
                print("------------------")
                print("Ganaste")
                game_over()

            else:
                if total > total_dealer:
                    print("Ganaste")
                    game_over()

                if total == total_dealer:
                    print("Empate")
                    game_over()      

        if total > total_dealer:
            print("Ganaste")
            game_over()

        if total == total_dealer:
            print("Empate")
            game_over()


def game_over():
    print("------------------")
    print("¿Volver a jugar?")
    print("a) Sí")
    print("b) No")
    vj = input()
    if vj == "a":
        print("------------------")
        bj()
    else:
        print("Fin del juego.")
        exit()

def valor_carta(m,jugador):
    cpu = random.randint(0,1)
    if jugador == 1:
        if m == "As":
            m = carta_as(m)
    if jugador == 0:
        if cpu == 0:
            if m == "As": m = 1
        if cpu == 1:
            if m == "As": m = 11
    if m == "J": m = 10
    if m == "Q": m = 10
    if m == "K": m = 10
    return m

def carta_dealer(o):
    print("------------------")
    print("Carta boca abajo del cruiper:",end=" ")
    print(o)

def carta_as(n):
    print("¿Que valor desea que sea el As?: ")
    print("a) 1")
    print("b) 11")
    op = input()
    if op == "a":
        n = 1
    elif op == "b":
        n = 11
    return n

bj()