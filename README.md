# Repositorio de entrega de proyectos bootcamp Data Science

## ÍNDICE

### -Hundir la flota

    Código en python del popular juego por turnos cuyo objetivo es de hundir los barcos del contrario,
    ubicados en coordenadas de un tablero, antes de ver hundidos los tuyos.
    
### -EDA sobre los precios de billetes de avión


#### -Introducción

    El objetivo del estudio es analizar el conjunto de datos de reservas de vuelos obtenido del sitio web "Ease My Trip"
    y realizar diversas pruebas estadísticas de hipótesis para obtener información significativa del mismo.
    Easemytrip" es una plataforma de Internet para reservar billetes de avión. Un estudio exhaustivo de los datos ayudará
    a descubrir información valiosa que será de enorme valor para los pasajeros.
        
#### -Preguntas de investigación

    El objetivo de nuestro estudio es responder a las siguientes preguntas de investigación:
    a) ¿Varía el precio con las aerolíneas?
    b) ¿Cómo se ve afectado el precio cuando los billetes se compran sólo 1 ó 2 días antes de la salida?
    c) ¿Cambia el precio del billete en función de la hora de salida y de llegada?
    d) ¿Cómo varía el precio con el cambio de origen y destino?
    e) ¿Cómo varía el precio del billete entre la clase Turista y la Business?

#### -Variables
    A continuación se explican las distintas variables del conjunto de datos:
        1) Aerolínea: El nombre de la compañía aérea se almacena en la columna compañía aérea. 
            Se trata de una característica categórica que incluye 6 aerolíneas       diferentes.
        2) Vuelo: Vuelo almacena información sobre el código de vuelo del avión. Es una característica categórica.
        3) Ciudad de origen: Ciudad desde la que despega el vuelo. Es una característica categórica que contiene 6 ciudades únicas.
        4) Hora de salida: se trata de una característica categórica derivada creada mediante la agrupación de periodos de tiempo en intervalos.
            Almacena información sobre la hora de salida y tiene 6 etiquetas de hora únicas.
        5) Paradas: Característica categórica con 3 valores distintos que almacena el número de paradas entre las ciudades de origen y destino.
        6) Hora de llegada: Se trata de una característica categórica derivada creada mediante la agrupación de intervalos de tiempo en intervalos.
            Tiene seis etiquetas de tiempo distintas y guarda información sobre la hora de llegada.
        7) Ciudad de destino: Ciudad en la que aterrizará el vuelo. Es una característica categórica que tiene 6 ciudades únicas.
        8) Clase: Característica categórica que contiene información sobre la clase de asiento; tiene dos valores distintos: Business y Economy.
        9) Duración: Una característica continua que muestra la cantidad total de tiempo transcurrido entre la salida y la llegada del vuelo de vuelta.
        10) Días restantes: Es una característica derivada que se calcula restando la fecha del viaje por la fecha de reserva.
        11) Precio: La variable objetivo almacena información del precio del billete.



