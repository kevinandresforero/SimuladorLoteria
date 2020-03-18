#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from random import randint
from tkinter import *

ventana= tk.Tk()
ventana.title("Loteria")
ventana.geometry("460x250+100+100")
ventana.configure(bg="black")    

l1 = tk.Label(ventana, text="\n Número-Código   \n9999-399\n\nTal Que : Número sea de 4 cifras  \nY\n Codigo sea < 400"
              , bg="black", fg="#ADFF2F").grid(row=0,column=0)
numeros = tk.Entry(ventana, width=20, bg="black", fg="#ADFF2F")
numeros.grid(row=2, column=0, pady=1)
intentos = 0

def jugar(boleto):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.geometry("700x450+450+100")
    nueva_ventana.configure(bg="black")
    
    estado = False
    contador = 0
    mensajeText = tk.Text(nueva_ventana)
    mensajeText.grid(
        row=0, 
        column=0,
        pady=4,
        padx=4)
    
    vistaV = tk.Scrollbar(nueva_ventana,command= mensajeText.yview)
    vistaV.grid(
        row=0, 
        column=1,
        sticky="nsew"
        )
    l1
    while estado == False:
        contador = contador +1
        nGanador = randint(0, 10000)
        cGanador = randint(0, 400)
        mGanador = "El boleto ganador en el intento "+str(contador)+" es: "+str(nGanador)+"-"+str(cGanador)
        
        print(str(boleto[0])+"-"+str(boleto[1])+" VS "+str(nGanador)+"-"+str(cGanador)+" En el intento "+str(contador))
        
        mensajeText.insert(END,mGanador)
        mensajeText.insert(END,"\n")
        nueva_ventana.mainloop
        if  int(boleto[0]) == nGanador and int(boleto[1])==cGanador:
            men = "\nGanaste en el intento: "+str(contador)
            mensajeText.insert(END,men)
            print(men)
            break

def Guardar():
    boleto = numeros.get()
    boleto = boleto.split("-")
    #       VALIDAR
    try:
        if int(boleto[0])/1 == int(boleto[0]) and int(boleto[1])/1 == int(boleto[1])and int(boleto[0])<10000 and int(boleto[1])<400:
            mensajeA = "Has adquirido satisfactoriamente el boleto con el número "+boleto[0]+" de la serie "+boleto[1]
            print(mensajeA)
            try:
                jugar(boleto)
            except:
                print("Error al intentar jugar")
        else:
            mensaje = "Debe ingresar el número de un boleto de lotería con el siguiente formato\nNúmero-Código   \n9999-399\n\nTal Que : Número < 10000  \nY\n Codigo sea < 400"
            print(mensaje)
    except:
        mensaje = "Debe ingresar el número de un boleto de lotería con el siguiente formato\nNúmero-Código   \n9999-399\n\nTal Que : Número < 10000  \nY\n Codigo sea < 400"
        print(mensaje)     

boton1 = tk.Button(ventana, text="Guardar", command=Guardar,bg="black", fg="#ADFF2F").grid(
        row=2, 
        column=1,
        sticky=tk.W,
        pady=4)

l2 = tk.Label(ventana, text="Ó\nIngrese el Número de números que quiere jugar", fg="#ADFF2F",bg="black")
l2.grid(row=3,column=0)
nn = tk.Entry(ventana, width=20, bg="black", fg="#ADFF2F")
nn.grid(row=4,column=0)

def jugarnn():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.geometry("700x450+555+100")
    nueva_ventana.configure(bg="black")
    
    numeros = nn.get()
    boletos = list(range(int(numeros)))
    aux = 0
    while aux < int(numeros):
        ni = randint(0, 10000)
        ci = randint(0, 400)
#        print(str(aux)+" ; "+str(nGanador)+"-"+str(cGanador))
        boletos[aux] = str(ni)+"-"+str(ci)
        print(boletos[aux])
        aux = aux + 1
    aux=0
    estado=False
    while estado == False:
        nGanador = randint(0, 10000)
        cGanador = randint(0, 400)
        boleto_ganador = str(nGanador)+"-"+str(cGanador)
#        print(boleto_ganador)
        mensajeText = tk.Text(nueva_ventana)
        mensajeText.grid(
            row=0, 
            column=0,
            pady=4,
            padx=4)
        
        contador = 0
        while aux < int(numeros):
            mGanador = "El boleto ganador en el intento "+str(contador)+" es: "+str(nGanador)+"-"+str(cGanador)
            print(mGanador)
            if boletos[aux] == boleto_ganador:
                mensajeText.insert(END,mGanador)            
                estado=True
                break 
            
            aux = aux +1
            contador = contador +1
            mensajeText.insert(END,"\n")

boton2 = tk.Button(ventana, text="Jugar N Números",bg="black", fg="#ADFF2F",command=jugarnn).grid(
        row=4, 
        column=1,
        sticky=tk.W,
        pady=4)
              
ventana.mainloop()

"""
Created on Thu Mar 12 09:42:28 2020
@author: Kevin
"""