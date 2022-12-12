import random
import numpy as np
import time


class escenario:
    '''
    Clase para gestionar los distintos tableros del juego
    Los tableros siempre tendran una dimensión de 10*10
    Un usuario ya sea jugador o computador
    Un tipo de ataque o defensa
    Sobre los distintos tableros se mostrará la situción de la batalla
    '''

    alto=10
    bajo=10
 
    def __init__(self, usuario:str, tipo_esc:str):

        self.usuario = usuario
        self.tipo_esc = tipo_esc
    
    def inicializar_tablero():
        tablero_ini = np.full((10,10), " ")
        return tablero_ini
    
    def colocar_barco(flota:list, tablero):
        for cord_barco in flota:
                for cord in cord_barco: 
                    tablero[cord] = "O"
        return tablero        

    def disparar(casilla,tablero,tablero_check,reg_disparo:list,reg_disparo_coord:list,target:list,barcos_obj:list):

        reg_disparo_coord.append(casilla)
        escenario.punteria_CPU(casilla,barcos_obj,reg_disparo_coord)
        if tablero_check[casilla] == "O":
            tablero[casilla] = "X"
            tablero_check[casilla] = "X"
            reg_disparo.append("X")
        elif tablero_check[casilla] == " ":
            tablero[casilla] = "-"
            tablero_check[casilla] = "-"
            reg_disparo.append("-")
        else:
            reg_disparo.append("K")
        for i,x in enumerate(target):
            for z in x:
                if z==casilla:
                       target[i].remove(z)
                       

    def filtro_cord (x:int,y:int):
        check=[0,1,2,3,4,5,6,7,8,9]
        if x not in check or y not in check:
            print('has introducido mal las coordenadas, vuelve a intenarlo'),{escenario.filtro_cord()}
        else: cord_disparo= (x,y)
        return cord_disparo

    def punteria_CPU (casilla:tuple,barcos_obj:list,reg:list):    
        for i in barcos_obj:  
            if casilla in i.posicion:
                i.vidas-=1
                if i.vidas==0:
                    i.estado='KO'
                    reg.extend(i.perimetro)







class usuario:

        def __init__(self,id:int,nombre:str,tipo_usario="Máquina",vidas=int(20)):
            self.id = id
            self.nombre = nombre          
            self.tipo_usuario = tipo_usario
            self.vidas=vidas

        def nivel_dificultad():
            print('Bien, has decidido jugar tú mismo contra la Máquina.')
            print('Ahora selecciona el nivel de dificultad 1, 2 ó 3')
            print('A mayor nivel de dificultad más disparos podrá hacer la Máquina aunque falle.\n')
            dificultad=['0','1','2','3']
            choice_dificultad=input()
            if choice_dificultad=='0':
                print('No hagas trampas, 0 no es una respuesta')
                print('Vas a empezar por el nivel 1\n')
                choice_dificultad=1
                return choice_dificultad
            elif choice_dificultad in dificultad:
                print('Ok, cargando algoritmo...')
                time.sleep (3)
                return choice_dificultad
            else: 
                print('Sólo los valores 1, 2 y 3 son aceptados, repite por favor.')
                usuario.nivel_dificultad()





class barco:

    Instancias_barco = []

    def __init__(self, eslora:int,posicion:list,perimetro:list,tipo:str,vidas:int,estado:str):
        self.eslora=eslora
        self.posicion=posicion
        self.perimetro=[]
        self.tipo=tipo
        self.vidas=vidas
        self.estado=estado
        self.__class__.Instancias_barco.append(self)


    def generar_b_aleatorio(xy_random:tuple,eslora:list):
        barco_random = []
        fila_random = xy_random[0]
        columna_random = xy_random[1]
        barco_random.append(xy_random)   
        rumbo_choice=[]
        if barco_random[0][0]>2:
             rumbo_choice.append('N')
        if barco_random[0][0]<7:
             rumbo_choice.append('S')
        if barco_random[0][1]>2:
             rumbo_choice.append('O')
        if barco_random[0][1]<7:
             rumbo_choice.append('E')
        rumbo=random.choice(rumbo_choice)
       
        while len(barco_random) < eslora:
            if rumbo == "N":
                fila_random = fila_random - 1
            if rumbo == "S":
                fila_random = fila_random + 1
            if rumbo == "E":
                columna_random = columna_random + 1
            if rumbo == "O":
                columna_random = columna_random - 1
       
            barco_random.append((fila_random,columna_random))
        return barco_random

    def generar_flota(barcos=[(1,4),(2,3),(3,2),(4,1)]):
        flota=[]
        flota_unica=[]
        insert_barco=[]
        flota_unica=[]
        insert_perimetro=[]     
        perimetro_unico=[]
        x=0
        for i in barcos:
            for x in range(0,i[0]):
                z=0
                while z==0:
                    z=1
                    dup=0
                    xy_random=barco.coord_aleatoria(flota_unica)
                    insert_barco=(barco.generar_b_aleatorio(xy_random,i[1]))
                    insert_perimetro=barco.perimetro(insert_barco)
                    for p in insert_perimetro:                                                 
                        if p in flota_unica: dup+=1
                    if dup==0:
                        flota_unica.extend(insert_barco),flota.append(insert_barco)
                        perimetro_unico.extend(insert_perimetro)
                        z=1
                    elif dup!=0: z=0               
        return flota

    def perimetro(list_coord:list):
        perimetro=[]
        x=[]
        y=[]
        for i in list_coord:
            x.append((int(i[0])))
            y.append(int(i[1]))
        if max(x)<9: x.append(max(x)+1)
        if max(y)<9: y.append(max(y)+1)  
        if min(x)>0: x.append(min(x)-1)
        if min(y)>0: y.append(min(y)-1)
        set_x=set(x)
        set_y=set(y)
        for x in set_x:
            for y in set_y:
                perimetro.append((x,y))
        return perimetro
        
    def check_hundido(list):
        if [] in list:
            list.remove([])
            return 'HUNDIDO,'
        else:
            return ', '           

    def set_barco(id:str,list_pos:list,list_obj:list):
        if id=="J1":
            for i,x in enumerate(list_pos):
                    list_obj[i].posicion=x
                    list_obj[i].perimetro=barco.perimetro(x)
        elif id=="J2":
                for i,x in enumerate(list_pos):
                    list_obj[i].posicion=x
                    list_obj[i].perimetro=barco.perimetro(x)

    def coord_aleatoria(list_block:list):
        x=[0,1,2,3,4,5,6,7,8,9]
        y=[0,1,2,3,4,5,6,7,8,9]
        list_coord=[(i,z) for i in x for z in y]
        unicas=barco.coord_unicas(list_block)

        for i in unicas:
            if i in list_coord:
                list_coord.remove(i)

        coord_random=random.choice(list_coord)

        return  coord_random

    def coord_unicas(list_coord:list):
        unicas = []
        for i in list_coord:
            if i not in unicas:
                unicas.extend(list_coord)
        return unicas