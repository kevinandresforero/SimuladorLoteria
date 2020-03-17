#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
import tkinter as tk
from tkinter import *

def consultar():
    comparador = randint(1000000, 9999999)
    
    numero = int(campo1.get())
    
    i = 1
    
    while comparador != numero:
        comparador = randint(1000000, 9999999)
        i = i + 1
        contador.set(i)
        print(i)
    
    resultado.set(f"Ganó en el intento {i} con el número: {comparador}")

def cerrar():
    marco.destroy()

marco = tk.Tk()
marco.title("Simulador de Loteria")
marco.geometry("500x400")
marco.configure(bg="black")

contador = tk.StringVar()
resultado = tk.StringVar()

l1 = tk.Label(marco, text="Ingrese numero de la loteria: ", bg="black", fg="red").grid(row=0, column=0)
l2 = tk.Label(marco, textvariable=resultado, bg="black", fg="red").grid(row=2, column=1)
l3 = tk.Label(marco, textvariable=contador, bg="black", fg="red").grid(row=2, column=0)

campo1 = tk.Entry(marco, bg="red", fg="black")
campo1.grid(row=0, column=1)

tk.Button(marco, text='Consultar', command=consultar, bg="black", fg="red").grid(row=0,
                                                                                 column=2,
                                                                                 sticky=tk.W,
                                                                                 pady=4)

tk.Button(marco, text='Cerrar', command=cerrar, bg="black", fg="red").grid(row=3,
                                                                           column=0,
                                                                           sticky=tk.W,
                                                                           pady=4)

marco.mainloop()

"""
Created on Thu Mar 12 09:42:28 2020
@author: Dragesteban
"""

