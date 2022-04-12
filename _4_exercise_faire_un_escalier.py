# exercise_faire_un_escalier


# Marche = 30 pixels en largeur et en hauteur
# Vous devez dessiner 5 marches
# Methode 1 de l'eexercice : creer l'escalier simplement

import turtle
"""
t = turtle.Turtle()         # Pour créer notre Turtle

t.forward(30)
t.left(90)
t.forward(30)
t.right(90)

t.forward(30)
t.left(90)
t.forward(30)
t.right(90)

t.forward(30)
t.left(90)
t.forward(30)
t.right(90)

t.forward(30)
t.left(90)
t.forward(30)
t.right(90)

t.forward(30)
t.left(90)
t.forward(30)
t.right(90)

t.forward(30)
turtle.done()               # Pour stabiliser notre fenêtre
"""


# Méthode 2 de l'exercice : creer l'escalier grâce à la boucle for
t = turtle.Turtle()         # Pour créer notre Turtle

for i in range(0, 5):
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)


t.forward(30)
turtle.done()               # Pour stabiliser notre fenêtre


# Méthode 3 de l'exercice creer l'escalier grâce à la fonction : escalier(taille, nmbre_de_marche )

t = turtle.Turtle() 

# definition de notre fonction
def escalier(taille, nmbre_de_marche):
    for i in range(nmbre_de_marche):
          t.forward(taille)
          t.left(90)
          t.forward(taille)
          t.right(90)
    t.forward(30)


escalier(30, 5)
turtle.done()



"""
# Amérlioration de la Méthode 3 de l'exercice creer l'escalier grâce à la fonction : escalier(taille, nmbre_de_marche )
# en reduisant la taille de la marche après chaque marche

t = turtle.Turtle() 

# definition de notre fonction
def escalier(taille, nmbre_de_marche):
    for i in range(nmbre_de_marche):
          t.forward(taille)
          t.left(90)
          t.forward(taille)
          t.right(90)
          taille -= 10             # ici on réduit la taille de la marche de 5 après chaque marche
    t.forward(taille)


escalier(50, 5)
turtle.done()
"""