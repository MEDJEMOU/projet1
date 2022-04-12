# exercice_dessigner_plusieurs_carre


# definir un nouvelle fonction : carres(taille_depart, nbre_de_carre)
# taille = (i+1)*taille_depart
# cette nouvelle fonction carres va appeler la precedent (carre)


import turtle


t = turtle.Turtle()


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

# definitaion de nouvelle fonction carres
def carres(taille_depart, nbre_de_carree):
    for i in range(0,nbre_de_carree):
        taille = (i+1)*(i+1)*taille_depart
        carre(taille)

carres(10, 10)
turtle.done()


# Pour multiplier les dimensions des carrés
"""
import turtle


t = turtle.Turtle()


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

# definitaion de nouvelle fonction carres
def carres(taille_depart, nbre_de_carree):
    for i in range(0,nbre_de_carree):
        taille = (i+1)*(i+1)*taille_depart
        carre(taille)

carres(10, 10)
turtle.done()
"""