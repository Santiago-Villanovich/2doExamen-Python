# 2doExamen-Python
Resolucion del segundo parcial de Introduccion a Python

PRÁCTICA 
Genere un programa que permita realizar la estimación de recorridos de una flota de camiones a lo largo de todo el país.  
- Cada clase Camion posee una patente, litros_disponibles, ciudad_actual, km_litro, vel_maxima y una clase Chofer (Con datos a definir por usted). Además, cada camión realiza recorridos que pasan por diversas ciudades entregando la mercadería de la empresa. 
- El programa debe permitir elegir un camión a partir de su patente y cargar un recorrido entre distintas ciudades (Se pueden prefijar cuatro o cinco ciudades por defecto con las respectivas distancias entre ellas). 
- Una vez escogido el camión y cargadas las ciudades destino, el programa devolverá a partir de un método llamado estimar_viaje(Camion, Ciudad[]):Estimacion los km por recorrer totales, el tiempo total estimado y si el combustible del camión alcanza para realizar todo el trayecto. Para hacer el cálculo utilizar la vel_maxima como velocidad promedio entre cada tramo y en cada ciudad sumar 60 minutos de parada. 
- Cada vez que se solicite el método estimar_viaje() se devolverá un objeto Estimacion con todos los datos solicitados,   antes de retornar el objeto, se deberá persistir en un archivo toda la información calculada junto a la patente del camión. 
- Permitir buscar todas las estimaciones realizadas para una patente X dentro del archivo guardado en el punto 4, mostrar por consola qué viajes superaron los 1000 km de distancia total y cuáles no. 
