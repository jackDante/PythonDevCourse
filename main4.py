

# soluzione compito 3:
# somma tutti gli elementi contenuti nella sequenza A
def somma_elementi(A):
    sum=0
    for i in range(len(A)):
        sum = sum + A[i]
    print(sum)

A = [10, 5, 2, 3, 50, 20, 10]
A.pop()
A.append(30)
print(A)
v=3
if v in A:
    A.remove(v)
print(A)
somma_elementi(A)

a=3223
print("{0} = {1}".format("ciao", a))
print("ciao = "+str(a))

#input -> X -> str(X) ->
def tre_input():
    B=[]
    B.append(int(float(input('inserisci numero1: '))))
    B.append(int(input('inserisci numero2: ')))
    B.append(int(input('inserisci numero3: ')))
    for i in range(len(B)):
        print("B[{0}] = {1}".format(i, B[i]))
    B.sort()

tre_input()

