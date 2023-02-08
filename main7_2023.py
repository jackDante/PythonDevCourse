# ___________ FILE __________________
# soluzione compito a casa:
"""
crea un file chiamato “leggimi.txt”,
apre il file in scrittura e scrive al suo interno i tuoi dati personali “nome, cognome e data nascita”
dopo aver scritto, fa una print() per stampare a video il contenuto del file
infine chiude ed elimina il file creato, quindi il file verrà cancellato dal disco.
"""
"""
import os

# With the code above, whether the file exists or the file doesn't exist in the memory,
# you can still go ahead and use that code. Just keep in mind that it will overwrite the file
# if it finds an existing file with the same name.
with open('leggimi.txt', "w", encoding="utf-8") as f:
    f.write("Giacomo, Usai e 18/07/1997")

with open('leggimi.txt', "r", encoding="utf-8") as f:
    print(f.readlines())

os.remove('leggimi.txt')
"""




"""__________________SNAKE PROJECT!________________________________________________________________________
# step 0:
Installing Pygame:
The first thing you will need to do in order to create games using Pygame is to install it on your systems.
"""
import pygame

"""
# step 1:
# Create the Screen:
To create the screen using Pygame, you will need to make use of the display.set_mode() function. 
Also, you will have to make use of the init()  and the quit() methods to initialize and 
uninitialize everything at the start and the end of the code. The update() method is used 
to update any changes made to the screen. There is another method i.e flip() that works similarly 
to the update() function. The difference is that the update() method updates only the changes 
that are made (however, if no parameters are passed, updates the complete screen) but the flip() method 
redoes the complete screen again.

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.quit()
quit()
"""

# step 2: __________________SNAKE PROJECT!______________________________
# --you will see that the screen that you saw earlier does not quit
# --Pygame provides an event called “QUIT”
"""
import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake game by Giacomo')
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()
"""

#step 3: __________________SNAKE PROJECT!______________________________
# Create the Snake:
# --definisco colori RGB=“Red Green Blue” (0 è nero, 255 è bianco)
# --To draw rectangles in Pygame, you can make use of a
# function called draw.rect() which will help yo draw the rectangle with the desired color and size.

import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Snake game by YOU')

blue = (0, 0, 255)
red = (255, 0, 0)
giallopython = (236, 187, 6)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis, giallopython, [200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()
