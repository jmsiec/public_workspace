"""
Created on Mon Apr 20 22:31:15 2020
@author: JM_si
Resumen:
Creamos un programa que genere una matriz de 0 y 1: Donde 0 sera un hoyo y 1 es tierra. 
Luego se pide la posicion al usuario, y se le indica si ha caido al hoyo o no. 
Se tiene hasta 3 intentos- 
"""

import random 


tabla=[[0,0,0],[0,0,0],[0,0,0]]

class NumeroRestringido(Exception): 
    "Excepcion de numero Erroneo: Coloca los numeros: 0, 1 o 2"
    pass 

def crear_tabla(tabla): 
#Produce una tabla random: 
    for k in range(0, 2): 
        for j in range(0, 2):
            numero=random.randrange(0,2)        
            tabla[j][k]=numero

# Nueva funcion contar hoyos             
def cuenta_hoyos(tabla):
    cuenta=0
    for casilla in tabla:
        for num in casilla:
            if (num==0): cuenta+=1
        
    return cuenta
  

def comienza_el_juego():
    vida=3
    while (vida>0): #Se tiene tres vidas
        print("Escriba la fila: ")
        try:  
            fila=int(input())
            if(fila <0 or fila >=3 ):
                raise NumeroRestringido("El numero es erroneo")               
        except ValueError: 
            print("Debes escribir un entero")
            
            
        print("Escriba la columna: ")
        try:  
            columna=int(input())
            if(fila <0 or fila >=3 ):
                raise NumeroRestringido("El numero es erroneo")                
            
        except ValueError: 
            print("Debes escribir un entero")
            
        print("escribiste la casilla: {0},{1}".format(fila,columna))
        if (tabla[fila][columna]==0) : 
            print("Uy!, caiste")
            vida=vida-1
            print("te queda {0} vidas".format(vida))
       
        else: print ("no te has caido, continua, te quedan saltar mas hoyos")
        
def main():         
    crear_tabla(tabla)
    num_hoyos=cuenta_hoyos(tabla)
    print ("El terreno tiene {0} hoyos".format(num_hoyos))
    print("Escriba la posicion donde no crea que haya un hoyo")
    comienza_el_juego()
    print("Game over")
    
    
main()

