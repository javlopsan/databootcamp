
import random
import time
from clases_v5 import *
from HF_Variables import *

print('Bienvenido\n')
print('Vas a jugar a Hundir la Flota contra la Máquina\n')
print('Las flotas están prepraradas\n')
print('Destruye la flota enemiga antes que destruyan la tuya\n')

tablero_1A=escenario.inicializar_tablero()
tablero_2A=escenario.inicializar_tablero()

flota_1=barco.generar_flota()
tablero_1D=escenario.inicializar_tablero()
flota_2=barco.generar_flota()
target_1=flota_2
target_2=flota_1

tablero_2D=escenario.inicializar_tablero()
reg_disparo_1=[]
reg_disparo_2=[]
reg_disparo_1_coord=[]
reg_disparo_2_coord=[]

escenario.colocar_barco(flota_1, tablero_1D)
escenario.colocar_barco(flota_2, tablero_2D)
barco.set_barco('J1',flota_1,objetos_j1)
barco.set_barco('J2',flota_2,objetos_j2)

vesus='0'


print ('Aquí abajo puedes ver la situación de tu flota\n')
print(tablero_1D)
print()
win=2
print('Marca 0 si quieres jugar contra la Máquina si no jugará la CPU por ti\n')
versus=str(input())
print()
dificultad=1
if versus=='0':
    turno=random.choice((1,2))
    dificultad=int(usuario.nivel_dificultad())

else:
    turno=1
   
if turno==1:
    print('!!!!Rápido!!! apunta y dispara, da el primer golpe\n')

else:
    print('OOOHHH NOOO!!! el adversario dispara primero, preparete\n')
    d=0
    limitador_rondas_extra=1
    while d==0:
        xy_random=barco.coord_aleatoria(reg_disparo_2_coord)
        escenario.disparar(xy_random,tablero_2A,tablero_1D,reg_disparo_2,reg_disparo_2_coord,target_2,objetos_j1)
        if reg_disparo_2[-1]=="X":
            if reg_disparo_2.count("X")==20:
                d=1
                print('Impacto!!!, hundieron tu último barco')
                print('Tus barcos antes de hundirse dispararon... para ganar debes acertras sin fallo 20 veces')
                print(tablero_1D)
                print()
            else:
                d=0             
                print(f'Impacto!!!{barco.check_hundido(target_2)}volverán a disparar')
                print('La situación de tu flota es:\n')
                print(tablero_1D)
                print()
        elif reg_disparo_2[-1]=="K":
            d=0
        else:
            if limitador_rondas_extra>=dificultad:
                d=1
                print('Fallaron, la situación de tu flota es\n')
                print(tablero_1D)
                print()
            else:
                d=0
                limitador_rondas_extra+=1
                print('Fallaron, la situación de tu flota es\n')
                print(tablero_1D)
                print()

v=0
while v==0:

    d=0
    while d==0:
        try:
            if versus=='0':
                print('Es tu turno, vamos a disparar')
                print('Para apuntar puedes ver aquí abajo el resultado de tus disparos\n')
                print(tablero_1A)
                print('Dame la coordenada X para el disparo\n')
                cord_x=int(input('Dame X: '))
                print('a continuacion dame la coordenada Y para el disparo\n')
                cord_y=int(input('Dame Y: '))
                escenario.disparar(escenario.filtro_cord(cord_x,cord_y),tablero_1A,tablero_2D,reg_disparo_1,reg_disparo_1_coord,target_1,objetos_j2)
            else:
                xy_random=barco.coord_aleatoria(reg_disparo_1_coord)
                escenario.disparar(xy_random,tablero_1A,tablero_2D,reg_disparo_1,reg_disparo_1_coord,target_1,objetos_j2)
        except: print('Asegurate, introduce valores del 0 al 9 en las coordenadas')
        
        print(tablero_1A)
        print()
        if reg_disparo_1[-1]=="X":
            if reg_disparo_1.count("X")==20:
                print('Impacto!!!, has ganado')
                d=1
                win=0
            else:
                d=0
                print(f'Impacto!!!{barco.check_hundido(target_1)}vuelve a disparar')
        else:
            d=1
            print('Ooooohhhh, fallaste, preparate para el ataque enemigo\n')

    if win==0:
        print('!!!!!!!VICTORIA!!!!!!')
        break
    d=0   

    limitador_rondas_extra=1
    while d==0:
            print('Es el turno de tu adversario, va a disparar\n')
            xy_random=barco.coord_aleatoria(reg_disparo_2_coord)
            escenario.disparar(xy_random,tablero_2A,tablero_1D,reg_disparo_2,reg_disparo_2_coord,target_2,objetos_j1)
            if reg_disparo_2[-1]=="X":
                if reg_disparo_2.count("X")==20:                    
                    d=1
                    win=1
                    print('Impacto!!!, hundieron tu último barco')
                    print(tablero_1D)
                    print()
                else:
                    d=0                
                    print(f'Impacto!!!{barco.check_hundido(target_2)}volverán a disparar')
                    print('La situación de tu flota es:\n')
                    print(tablero_1D)
                    print()
            elif reg_disparo_2[-1]=="K":
                d=0
            else:
                if limitador_rondas_extra>=dificultad:
                    d=1
                    print('Fallaron, la situación de tu flota es\n')
                    print(tablero_1D)
                    print()                    
                else:
                    limitador_rondas_extra+=1
           
                    d=0
                    print('Fallaron, la situación de tu flota es\n')
                    print(tablero_1D)
                    print()
    if win==1:
        print('!!!!!!!PERDISTE!!!!!!')
        break 


    
