# exercice_dessigner_un_carre


# definir un nouvelle fonction : carre(30, 5)
# appeler la fonction avec le nombre de pixels = 100


import turtle


t = turtle.Turtle()
def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


carre(100)
turtle.done()