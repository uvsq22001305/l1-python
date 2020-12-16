import tkinter as tk
import random as rd

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


color = get_color(rd.randint(0,255),rd.randint(0,256),rd.randint(0,256))
def draw_circle(x, y, ray, color):
    '''fonction définie dans l'exercice des cercles concentriques'''
    canvas.create_oval(x-ray, y-ray, x+ray, y+ray, fill=color)

def draw_new_circle(event):
  if(event.x < 250):
    draw_circle(event.x, event.y, 50, "blue")
  else:
    draw_circle(event.x, event.y, 50, "red")


racine = tk.Tk()
canvas = tk.Canvas(racine, width=500, height=500, bg="black")
canvas.create_line(250, 0, 250, 500, fill=get_color(rd.randint(0,255),rd.randint(0,256),rd.randint(0,256)))
canvas.bind("<Button-1>", draw_new_circle)
canvas.grid()
racine.mainloop()