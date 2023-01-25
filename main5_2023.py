# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.
# CLASSE (famiglia) -> OGGETTO?    --> ATTRIBUTO

# qui definisco la classe

class Persona:
    # funzione che inizializza gli attributi della classe
    def __init__(self, name, age, indirizzo):
        self.name = "Giulio"
        self.age = age
        self.indirizzo = indirizzo

    def mia_funz_saluta_tutti(self):
        print("Ciao a tutti!!!")


# qui creo un oggetto appartenente alla classe sopra definita
p1 = Persona("giacomo", 99, "via tutto")  # è un oggetto
print(p1)
print(p1.name)
p1.name = "Matteo"
print(p1.name)
print(p1.age)
# print(p1.altezza) questo attributo non è presente nella classe Persona

p1.age = 25
print(p1.age)

p1.mia_funz_saluta_tutti()

# ________________________________________________________ FILE
"""
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
"r" - Lettura - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Scrittura - Opens a file for writing, creates the file if it does not exist
"x" - Creazione nuovo file - Creates the specified file, returns an error if the file exists
"""

#f = open("giacomo.txt", "x") # crea file

f = open("giacomo.txt", "w")
f.write("weiweiweiweiweiwei")
print(type(f))
f = open("giacomo.txt", "r")
print(f.readlines())
f.close()