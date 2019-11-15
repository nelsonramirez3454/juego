#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Game():

    def __init__(self):
        #Incicializamos objeto Game con la matriz de juego y el numero de 0s y puntos actuales
        #inicialmente como valor por defecto a 0

        self.mat=[[0 for x in range(9)] for x in range(9)]
        self.nceros=0
        self.puntos=0

    def facil(self):
        #llena la matriz para el modo facil numeros entre 1-3

        self.nceros=0
        self.puntos=0
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.mat[i][j]= random.randrange(1,4)

    def muyfacil(self):
        #llena la matriz de juego para el nivel oculto.

        self.nceros=0
        self.puntos=0
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.mat[i][j]= 1

        for i in range(len(self.mat)):
            for j in range(i,len(self.mat[0])):
                    if(((i+j)%2)==0):
                        self.mat[i][j]=2
                    else:
                        self.mat[i][j]=3

    def intermedio(self):
        #llena la matriz para el modo facil numeros entre 1-4
        self.nceros=0
        self.puntos=0
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.mat[i][j]= random.randrange(1,5)

    def dificil(self):
        #llena la matriz para el modo facil numeros entre 1-5

        self.nceros=0
        self.puntos=0
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.mat[i][j]= random.randrange(1,6)

    def tf1(self):
        #llena la matriz para el modo tablero fijo 1

        self.nceros=0
        self.puntos=0
        x=0
        while(x<5): # va recorriendo por capas la matriz y llenandola de cuadrados cada vez ms pequeños
            for i in range(x,len(self.mat)-x,1):
                for j in range(x,len(self.mat[0])-x,1):
                    if(x==0):
                        self.mat[i][j]=1
                    elif(x==1):
                        self.mat[i][j]=2
                    elif(x==2):
                        self.mat[i][j]=3
                    elif(x==3):
                        self.mat[i][j]=1
                    else:
                        self.mat[i][j]=2
            x += 1

    def tf2(self):
        #llena la matriz para el modo tablero fijo 2, llenamos toda la matriz de 4s bolas mas bundantes y el resto
        #se introducen a mano

        self.nceros=0
        self.puntos=0
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.mat[i][j]= 4
        #1
        self.mat[0][4]=1
        self.mat[1][3]=1
        self.mat[1][5]=1
        self.mat[2][6]=1
        self.mat[2][2]=1
        self.mat[3][7]=1
        self.mat[3][1]=1
        self.mat[4][8]=1
        self.mat[4][0]=1
        self.mat[5][1]=1
        self.mat[5][7]=1
        self.mat[6][2]=1
        self.mat[6][6]=1
        self.mat[7][3]=1
        self.mat[7][5]=1
        self.mat[8][4]=1

        self.mat[3][4]=1
        self.mat[4][5]=1
        self.mat[4][3]=1
        self.mat[5][4]=1

        #2
        self.mat[1][4]=2
        self.mat[2][5]=2
        self.mat[2][3]=2
        self.mat[3][2]=2
        self.mat[3][6]=2
        self.mat[4][1]=2
        self.mat[4][7]=2
        self.mat[5][2]=2
        self.mat[5][6]=2
        self.mat[6][3]=2
        self.mat[6][5]=2
        self.mat[7][4]=2

        self.mat[4][4]=2

        #3
        self.mat[2][4]=3
        self.mat[3][5]=3
        self.mat[3][3]=3
        self.mat[4][2]=3
        self.mat[4][6]=3
        self.mat[5][3]=3
        self.mat[5][5]=3
        self.mat[6][4]=3

    def tf3(self):
        #recorre la matriz de la partida y la va llenando en funcion a la pariedad de la suma de sus cordenadas
        #dejando un damero

        self.nceros=0
        self.puntos=0
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if(((i+j)%2)==0):
                    self.mat[i][j]=1
                else:
                    self.mat[i][j]=2
        self.mat[3][6]=1 #dejamos un valor que permita jugar ya que sin el no tendriamos movimientos

    def mostrar(self, modo, mispuntos):
        #procedimiento para mostrar por pantalla como esta la matriz actual del juego y las puntuaciones actuales e historicas

        if(modo=="facil"):
            x=0
        elif(modo=="intermedio"):
            x=1
        elif(modo=="dificil"):
            x=2
        elif(modo=="tfijo1"):
            x=3
        elif(modo=="tfijo2"):
            x=4
        elif(modo=="tfijo3"):
            x=5
        else:
            x=6

        print "      -----------------------------------"
        for i in range((len(self.mat))-1,-1,-1):
            print (i+1),"  |",
            for j in range(len(self.mat[0])):
                if(self.mat[i][j]==1):
                    print "\033[31m ❶ \033[0m",
                elif(self.mat[i][j]==2):
                    print "\033[32m ❷ \033[0m",
                elif(self.mat[i][j]==3):
                    print "\033[33m ❸ \033[0m",
                elif(self.mat[i][j]==4):
                    print "\033[34m ❹ \033[0m",
                elif(self.mat[i][j]==5):
                    print "\033[35m ❺ \033[0m",
                else:
                    print " ○ ",

            if(i==7):
                print "|","  La puntuacion actual es",self.puntos
            elif(i==3):
                print "|","  La puntuacion maxima es", mispuntos.listapuntos[x][1]
            else:
                print "|"

        print "      -----------------------------------"
        print "       1   2   3   4   5   6   7   8   9 "
        print"\n"

    def cerosup(self):
        #deplaza los ceros a la parte superior de la pantalla

        cer=[0 for x in range(len(self.mat))]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if(self.mat[i][j]==0):
                    cer[j]=cer[j]+1

        for x in range(len(self.mat)):
            for i in range(len(self.mat)):
                for j in range(len(self.mat[0])):
                    if(self.mat[i][j]==0):
                        for k in range(i,len(self.mat[0])-1):
                            self.mat[k][j]=self.mat[k+1][j]

        for j in range(len(self.mat[0])):
            for i in range(len(self.mat)-1,-1,-1):
                if(cer[j]!=0):
                    self.mat[i][j]=0
                    cer[j]=cer[j]-1

    def columns(self):
        c=0
        for j in range(len(self.mat[0])):
            x=0
            for i in range(len(self.mat)):
                x=x+self.mat[i][j]
            if(x==0):
                c=c+1

        for r in range(len(self.mat)):
            for j in range(len(self.mat)):
                x=0
                for i in range(len(self.mat[0])):
                    x=x+self.mat[i][j]
                if(x==0):
                    for b in range(j,len(self.mat[0])-1):
                        for a in range(len(self.mat)):
                            self.mat[a][b]=self.mat[a][b+1]

        for j in range(len(self.mat[0])-1,(8-c),-1):
            for i in range(len(self.mat)):
                self.mat[i][j]=0

    def comparar(self,i,j,valor):
        if(self.mat[i][j]!=0):
            if(((j+1)<len(self.mat[0]))):
                if(valor==(self.mat[i][j+1])):
                    self.mat[i][j]=0
                    self.comparar(i,j+1,valor)
                    if((j+1)<len(self.mat[0])):
                        self.mat[i][j+1]=0

            if((0<=(j-1))):
                if(valor==(self.mat[i][j-1])):
                    self.mat[i][j]=0
                    self.comparar(i,j-1,valor)
                    if((j-1)>=0):
                        self.mat[i][j-1]=0

            if(((i+1)<len(self.mat))):
                if(valor==(self.mat[i+1][j])):
                    self.mat[i][j]=0
                    self.comparar(i+1,j,valor)
                    if((i+1)<len(self.mat)):
                        self.mat[i+1][j]=0

            if((0<=(i-1))):
                if(valor==(self.mat[i-1][j])):
                    self.mat[i][j]=0
                    self.comparar(i-1,j,valor)
                    if((i-1)>=0):
                        self.mat[i-1][j]=0

    def point(self):
        x=0
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if(self.mat[i][j]==0):
                    x=x+1
        self.puntos=self.puntos+((x-self.nceros)*(x-self.nceros)*5)
        self.nceros=x

    def fin(self, modo,mispuntos):

        if(modo=="facil"):
            md=0
        elif(modo=="intermedio"):
            md=1
        elif(modo=="dificil"):
            md=2
        elif(modo=="tfijo1"):
            md=3
        elif(modo=="tfijo2"):
            md=4
        elif(modo=="tfijo3"):
            md=5
        else:
            md=6

        end=1
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if(self.mat[i][j]!=0):
                    if(((j+1)<len(self.mat[0]))and(self.mat[i][j]==self.mat[i][j+1])):
                        end=0
                    if((0<=(j-1))and(self.mat[i][j]==self.mat[i][j-1])):
                        end=0
                    if(((i+1)<len(self.mat))and(self.mat[i][j]==self.mat[i+1][j])):
                        end=0
                    if((0<=(i-1))and(self.mat[i][j]==self.mat[i-1][j])):
                        end=0

        if(end==1):
            print "No hay mas movimientos.\n"
            x=0
            for i in range(len(self.mat)):
                for j in range(len(self.mat[0])):
                    if(self.mat[i][j]!=0):
                        x=x+1

            if((2000-(x*x*10))>=0):
                self.puntos=self.puntos+(2000-(x*x*10))

            if(mispuntos.listapuntos[md][1]<self.puntos):
                print"Enhorabuena has superado la puntuacion maxima!!!"
                mispuntos.listapuntos[md][1]=self.puntos
            else:
                print "No superaste tu mejor marca."

        return end

    def jugada(self,modo,mispuntos):
        x=0
        while(x!=1):
            cord=raw_input("Intrduce las codenadas [i j]:  ")
            try:
                numbers = map(int, cord.split())
                i=numbers[0]
                j=numbers[1]
                i-=1
                j-=1
                if(len(numbers)==2):
                    if((0<=i)and(i<9)and(0<=j)and(j<9)):
                        x=1
                    if((i==-1)and(j==-1)):
                        return 0
            except:
                x=0
        print ""
        valor=self.mat[i][j]
        self.comparar(i,j,valor)
        self.cerosup()
        self.columns()
        self.point()
        self.mostrar(modo, mispuntos)
        return 1

    def partida(self, modo,mispuntos):
        self.mostrar(modo, mispuntos)
        self.puntos=0
        self.nceros=0

        end=0
        while(end==0):
            x=self.jugada(modo,mispuntos)
            end=self.fin(modo, mispuntos)
            #self.mostrar(modo, mispuntos)
            if(x==0):
                break
        if(end==1):
            print "Tu puntuacion final es:",self.puntos,"\n"
            comprobar=False
            while(comprobar==False):
                nueva=raw_input("Nueva partida (1=Si 0=Menu)?  ")
                try:
                    new= int(nueva)
                except:
                    new=2
                if(new==0):
                    comprobar=True
                if(new==1):
                    comprobar=True
            return new

class Ranking():

    def __init__(self):
        self.listapuntos=[["Facil: ",0],["Intermedio: ",0],["Dificil: ",0],["Tablero Fijo 1: ",0],["Tablero Fijo 2: ",0],["Tablero Fijo 3: ",0],["Nivel oculto: ",0]]
        try:
            fread=open("puntuaciones.txt")

            for i in range(len(self.listapuntos)):
                try:
                    self.listapuntos[i][1]=int(fread.readline())
                except:
                    self.listapuntos[i][1]=0
        except:
            print "No hay archivo exixtente se creara nuevo archivo."

    def mostrar(self):
        print "\n\tEl Ranking de maximas pruntuaciones es: "
        print "\t_______________________________________\n"
        for i in range(len(self.listapuntos)):
            for j in range(len(self.listapuntos[0])):
                if(i==0):
                    print self.listapuntos[i][j],"\t\t\t",
                elif(i==1):
                    print self.listapuntos[i][j],"\t\t",
                elif(i==2):
                    print self.listapuntos[i][j],"\t\t\t",
                elif(i==6):
                    print self.listapuntos[i][j],"\t\t",
                else:
                    print self.listapuntos[i][j],"\t",
            print ""

    def borrar(self):
        for i in range(len(self.listapuntos)):
            self.listapuntos[i][1]=0
        print "Se han borrado las puntuaciones."

    def guardar(self):
        fwrite=open("puntuaciones.txt", "w")
        for i in range(len(self.listapuntos)):
            puntos=str(self.listapuntos[i][1])
            fwrite.write(puntos+"\n")
        fwrite.close()

    def niveloculto(self):
        activar = True
        for i in range(len(self.listapuntos)-1):
            if (self.listapuntos[i][1]==0):
                activar = False

        return activar
