

# soluzione compito 2: fattoriale di 5! = 120
# 5! = 5*4*3*2*1 = 120
def funzione_fattoriale():
   fattoriale = 1
   for c in range(2, 6):
       print(c)
       fattoriale = c * fattoriale
   print(fattoriale)


def fatt(n):
   f = 1
   for c in range(2, n+1):
       f = c * f
       print(c)
       print(f)
   print(f)

# Serie di Fibonacci fino a n

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a = b
        b = a+b

#fib(1000)

"""
"""

if __name__ == '__main__':
    # a = int(input('inserisci numero: ')) # input richiede all'utente l'inserimento da tastiera
    # fib(a)
#_________ Lezione 3: sequenze (ordinate per posizione)
    # definisco una sequenza (chiamata anche array)
    città = ['Genova', 'Milano', 'Roma']
    # stampo in primo elemento
    print(città[0])
    # stampo in secondo
    print(città[1])
    # interrogo chiedendo se l'elemento "Roma" è nella sequenza: riceverò True (se presente) sennò False
    print("Giovanni" in città)
    # lunghezza della sequenza usando la funzione "len()"
    print(len(città))
    # definisco una sequenza di numeri e calcolo minimo e max
    A = [23, 302, 9]
    print(A)
    print(min(A))
    print(max(A))
    A[0] = 1000
    print(A)
    print(sorted(A))
    A.append(4)
    print(A)
    print(type(A))
    print(type(città))






