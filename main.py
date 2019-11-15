#!/usr/bin/env python
# -*- coding: utf-8 -*-
from obj import Game
from obj import Ranking

mimatriz= Game()
mispuntos= Ranking()

def menuprincipal():
    #Funcion del menu principal
    print "\n\n\n\n\n"
    x=0
    while(x==0):#muestra el menu hasta obtener una respuesta valida.
        print "\t ***Rompe Bolas***"
        print "\t ================="
        print "Menu:"
        print "\t\033[32m 1. Facil:\033[0m"
        print "\t\033[33m 2. Intermedio:\033[0m"
        print "\t\033[31m 3. Dificil:\033[0m"
        print "\t\033[34m 4. Tableros Fijos:\033[0m"
        print "\t 5. Mejores Puntuaciones:"
        print "\t 6. Borrar mejores puntuaciones:"

        if(mispuntos.niveloculto()==True):#comprueba si ya se tiene acceso al nivel oculto
            print "\t\033[35m 7. *Nivel oculto*\033[0m"

        print "\t 0. Salir.\n"
        menu1=raw_input("Introduce la opcion a la que quieras aceder:  ")
        if(menu1=="7"):
            if(mispuntos.niveloculto()==True):#comprueba si ya se tiene acceso al nivel oculto
                x=1
                menu=7
        else:#comprueba que los valores introducidos estan en el rango valido.
            try:
                menu=int(menu1)
                if((menu>=0)and(menu<=6)):
                    x=1
            except:
                x=0

    #el menu realiza las distintas tareas en funcion a la opcion seleccionada.
    if(menu==1):
        print "\n"
        new=1
        while(new==1):
            mimatriz.facil()
            new= mimatriz.partida("facil",mispuntos)
        menuprincipal()

    elif(menu==2):
        print "\n"
        new=1
        while(new==1):
            mimatriz.intermedio()
            new= mimatriz.partida("intermedio",mispuntos)
        menuprincipal()

    elif(menu==3):
        print "\n"
        new=1
        while(new==1):
            mimatriz.dificil()
            new= mimatriz.partida("dificil",mispuntos)
        menuprincipal()

    elif(menu==4):
        submenu()

    elif(menu==5):
        print "\n"
        mispuntos.mostrar()
        menuprincipal()

    elif(menu==6):#confirmacion para la opcion de borrar datos.
        print "\n"
        pregunta=False
        while(pregunta==False):
            respuesta=raw_input("Seguro que desea borrar los datos (S=si /N=no):  ")
            if(respuesta=="S"):
                pregunta=True
                mispuntos.borrar()
            elif(respuesta=="N"):
                pregunta=True
            else:
                pregunta=False
        menuprincipal()

    elif(menu==0):#con la opcion 0 se guradan los datos actualizados al salir.
        print "\n"
        mispuntos.guardar()
        print "Hata luego."

    else:
        print "\n"
        new=1
        while(new==1):
            mimatriz.muyfacil()
            new= mimatriz.partida("muyfacil",mispuntos)
        menuprincipal()

def submenu():
    #segundo menu del programa, muestra las opciones de tableros fijos.
    print "\n\n\n\n\n"
    x=0
    while(x==0):#funcionamiento similar al menu principal
        print "\t ***Tableros Fijos***"
        print "\t ===================="
        print "SubMenu:"
        print "\t 1. Cuadrado con 3 colores."
        print "\t 2. Rombo con 4 colores."
        print "\t 3. Casi-damero, con 2 colores."
        print "\t 0. Volver."
        menu1=raw_input("Introduce la opcion a la que quieras aceder:  ")
        try:
            menu=int(menu1)
        except:
            x=0
        if((menu>=0)and(menu<=3)):#comprueba que la estada se adapta al rango de valores.
            x=1

    if(menu==1):
        new=1
        while(new==1):
            mimatriz.tf1()
            new= mimatriz.partida("tfijo1",mispuntos)
        menuprincipal()
    elif(menu==2):
        new=1
        while(new==1):
            mimatriz.tf2()
            new= mimatriz.partida("tfijo2",mispuntos)
        menuprincipal()
    elif(menu==3):
        new=1
        while(new==1):
            mimatriz.tf3()
            new= mimatriz.partida("tfijo3",mispuntos)
        menuprincipal()
    else:
        menuprincipal()

#Llamada al menu que inicia el juego
menuprincipal()

#Notas para Jose:
#   Buscar Nivel Oculto para completar el conjunto de niveles
#   Documentacion interna y externa. No lo dejes para el final
#   Posibles mejoras ??