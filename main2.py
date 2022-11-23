# GU 23/11/22

# LEZIONE 2 -----------------------------------------

# soluzione compito 1
def concatenazionestringhe(stringa1, stringa2, stringa3):
    s = stringa1 + stringa2 + stringa3
    print(s)


# soluzione compito 1
def somma_tre_numeri(x, y, z):
    somma = x+y+z
    print(somma)


# funzione che illustra il controllo If
def condizioneIF():
    i = 10
    if i > 15:
        print("10 is less than 15")
        i = 1
    print("I am Not in if")


# funzione che illustra il ciclo FOR
def cicloFOR():
    for c in range(11):
        print(c/2)


# funzione che illustra come ragiona il comando "in range" che ci consente di scegliere inizio e fine del ciclo.
# il seguente esempio mostra come partire da 5 e fermarsi a 10, quindi stamperà a video i valori 5, 6, 7, 8, 9, 10
# Pertanto "in range" ci consente di scegliere i limiti del nostro range.
def in_range_cicloFOR():
    for c in range(5, 11):
        print(c)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #concatenazionestringhe("Ciao   ", "Mondo!")
    #condizioneIF()
    #cicloFOR()
    #in_range_cicloFOR()
    a = input('inserisci numero: ') # input richiede all'utente l'inserimento da tastiera
    print(type(a))

