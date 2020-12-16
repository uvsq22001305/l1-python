import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()
root.title("DESSIN")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief=tk.GROOVE, bd=1)


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


couleur=get_color(random.randint(0,257),random.randint(0,257),random.randint(0,257))

def choix_couleur():
    global couleur
    couleur=input()

def create_button(text, fonction, i, j):
    bouton = tk.Button(text=text, command = fonction, font = ("Helvetica", "30"), activeforeground="red", activebackground="black", padx=100)
    bouton.grid(column=i, row=j)
    return bouton

def dessine_cercle():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    objet.append(canvas.create_oval(x - 50, y - 50, x + 50, y + 50, fill=couleur))

def dessine_carre():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    objet.append(canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50, fill=couleur))

def dessine_croix():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    objet.append(canvas.create_line(x - 50, y - 50, x + 50, y + 50, fill=couleur))
    objet.append(canvas.create_line(x - 50, y + 50, x + 50, y - 50, fill=couleur))


def undo():
    """ supprimer la derniere figure"""
    if len(objet) == 0:
        return
    canvas.delete(objet[-1])
    del objet[-1]
    if len(objet) == 0:
        return

    if canvas.type(objet[-1]) == "line":
        canvas.delete(objet[-1])
        del objet[-1]



# Début de votre code


objet = []


cercle = create_button("cercle", dessine_cercle, 0, 1)
carre = create_button("carre",   dessine_carre, 0, 2)
croix = create_button("croix",   dessine_croix, 0, 3)
choix = create_button("choisir une couleur",  choix_couleur, 1, 0)
retour = create_button("annuler",  undo, 2, 0)
# Fin de votre code

canvas.grid(column=1, row = 1, rowspan=3)
canvas.create_oval(150, 150, 250, 250)
root.mainloop()