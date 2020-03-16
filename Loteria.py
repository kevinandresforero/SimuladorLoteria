#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
import tkinter as tk
#from tkinter import *

ventana= tk.Tk()
ventana.title("Loteria")
ventana.geometry("500x500")
ventana.configure(bg="black")
ventana.mainloop()

comparador = randint(1000000, 9999999)

numero = int(input("Escriba el número para la lotería: "))

i = 1

while comparador != numero:
    comparador = randint(1000000, 9999999)
    i = i + 1
    print("Intento: ", i)

print("Ganó en el intento: ", i, " con el número: ", comparador)

"""
Created on Thu Mar 12 09:42:28 2020
@author: Kevin
"""

