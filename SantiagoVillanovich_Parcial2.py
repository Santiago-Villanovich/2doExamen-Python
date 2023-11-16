import re
import json
from datetime import timedelta
import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


class Camion:

    def __init__(self,patente, litros_disponibles, ciudad_actual, km_litro, vel_maxima,chofer) -> None:
        self._patente = patente
        self._litros_disponibles = litros_disponibles
        self._ciudad_actual = ciudad_actual
        self._km_litro = km_litro
        self._vel_maxima = vel_maxima
        self.setChofer(chofer)
        print(f"Se creo Camion - patente: [{self._patente}]")

    def setChofer(self,chofer):
        self._chofer = chofer
    def Chofer(self):
        return self._chofer
    
    def setRecorrido(self, ciudades):
        self._recorrido = ciudades
    def Recorrido(self):
        return self._recorrido
    

    def km_totales(self):
        """Calcula y retorna el total de kilometros de el recorrido del camion"""
        try:
            km_totales = sum(self._ciudad_actual._distancias[ciudad] for ciudad in self._recorrido if ciudad in self._ciudad_actual._distancias)
            return int(km_totales)
        except Exception as e:
            print(f"Error al calcular kilometraje: {e}")

    def estimar_viaje(self):
        """Se estima los datos principales del viaje del camion y se realiza una persistencia en un archivo .json"""
        try:
            km_totales = self.km_totales()
            tiempo_estimado = timedelta(minutes=(km_totales / self._vel_maxima) * 60)
            tiempo_estimado += timedelta(minutes=len(self._recorrido) * 60)

            combustible_necesario = km_totales / self._km_litro
            if combustible_necesario > self._litros_disponibles:
                combustible_suficiente = False
            else:
                combustible_suficiente = True

            # Persisto la informacion del viaje
            self.persistir_estimacion( Estimacion(km_totales, tiempo_estimado, combustible_suficiente))

            return Estimacion(km_totales, tiempo_estimado, combustible_suficiente)
        
        except Exception as e:
            print(f"Error en la estimacion de viaje: {e}")
        
    def persistir_estimacion(self, estimacion):
        """Se realiza la persistencia de un objeto estimacion en un archivo .json"""
        try:   
            data = {"patente": self._patente,
                    "km_totales": estimacion.km_recorrido,
                    "tiempo_estimado": str(estimacion.tiempo_estimado),
                    "combustible_suficiente": estimacion.is_combustible_suficiente}
            
            my_path = "Estimaciones_viajes.json"
            
            if os.path.exists(my_path):
                with open(my_path, 'r') as file:
                    estimaciones = json.load(file)
            else:
                estimaciones = []
            
            estimaciones.append(data)
            
            with open(my_path, 'w') as file:
                json.dump(estimaciones, file, indent=4)
  
        except Exception as e:
            print(f"Error al persistir la estimación: {e}")
    
class Estimacion:
    def __init__(self, km_totales, tiempo_estimado, combustible_suficiente):
        self.km_recorrido = km_totales
        self.tiempo_estimado = tiempo_estimado
        self.is_combustible_suficiente = combustible_suficiente
    
    def detalle(self):
        return f"Distancia: {self.km_recorrido} Km\nTiempo estimado: {self.tiempo_estimado}\nAlcanza combustible: {self.is_combustible_suficiente}"

    @classmethod
    def buscar_estimaciones(cls,patente):
        """Se busca e imprime en pantalla el las estimaciones almacenadas en el archivo .json"""
        try:
            with open("Estimaciones_viajes.json" , 'r') as file:
                estimaciones = json.load(file)
                                    
            estimaciones_Patente = list(filter(lambda e: e["patente"] == patente, estimaciones))
            estimaciones_superadas = list(filter(lambda e: e["km_totales"] > 1000, estimaciones))
            estimaciones_no_superadas = list(filter(lambda e: e["km_totales"] <= 1000, estimaciones))

            print(f"Estimaciones previas patente: {patente}")
            for p in estimaciones_Patente:
                print(f"Kilometros:",p["km_totales"],end =' - ') 
                print(f"Tiempos: ",p["tiempo_estimado"],end =' - ')
                print(f"Combustible:",p["combustible_suficiente"])

            print(f"\nEstimaciones con mas de 1000km")
            if  not estimaciones_superadas:
                print("Sin estimaciones")
            else:
                for p in estimaciones_superadas:
                    print(f"Kilometros:",p["km_totales"],end =' - ') 
                    print(f"Tiempos: ",p["tiempo_estimado"],end =' - ')
                    print(f"Combustible:",p["combustible_suficiente"])

            print(f"\nEstimaciones con menos de 1000km")
            if  not estimaciones_no_superadas:
                print("Sin estimaciones")
            else:
                for p in estimaciones_no_superadas:
                    print(f"Kilometros:",p["km_totales"],end =' - ') 
                    print(f"Tiempos: ",p["tiempo_estimado"],end =' - ')
                    print(f"Combustible:",p["combustible_suficiente"])

        except Exception as e:
            print(f"Error al buscar estimaciones: {e}")

class Chofer:
    def __init__(self,nombre, apellido, dni, telefono) -> None:
        self._nombre= nombre
        self._apellido = apellido
        self._dni = dni
        self._telefono = telefono
        print(f"Se creo Chofer - {self._nombre} {self._apellido}, Dni:{self._dni}, Tel:{self._telefono}")

    def NombreApellido(self):
        return f"{self._nombre} {self._apellido}"

class Ciudad:
    def __init__(self,nom,distancias) -> None:
        self._nombre = nom
        self._distancias = distancias

#DEFINO LAS CIUDADES POSIBLES
ciudad1= Ciudad("Lujan", {"CABA": 75, "Lobos": 90, "Campana": 51, "La Plata": 128})
ciudad2 = Ciudad("CABA",{"Lujan": 75, "Lobos": 105, "Campana": 80, "La Plata": 60})
ciudad3 = Ciudad("Lobos",{"CABA": 105, "Lujan": 90, "Campana": 70, "La Plata": 150})
ciudad4 = Ciudad("Campana",{"CABA": 75, "Lobos": 90, "Lujan": 51, "La Plata": 170})
ciudad5 = Ciudad("La Plata",{"CABA": 60, "Lobos": 150, "Campana": 170, "Lujan": 128})
Ciudades = [ciudad1,ciudad2,ciudad3,ciudad4,ciudad5]

##GENERO CHOFERES
chofer1 = Chofer("Juan", "Pérez", "12345678", "5552-1234")
chofer2 = Chofer("Ana", "González", "23456789", "5545-5678")
chofer3 = Chofer("Pedro", "Sánchez", "34567890", "5555-9012")
chofer4 = Chofer("María", "López", "45678901", "5565-3456")
##GENERO CAMIONES
camion1 = Camion("ABC123", 100, ciudad1, 8, 120,chofer1)
camion2 = Camion("DEF456", 80, ciudad1, 6, 100,chofer2)
camion3 = Camion("GHI789", 120, ciudad2, 10, 150,chofer3)
camion4 = Camion("JKL012", 90, ciudad2, 7, 110,chofer4)

lista_camiones = [camion1, camion2, camion3, camion4]

def validar_patente(patente):
    """Se valida el formato de la patente y luego su existencia"""
    try:
        if re.match('^[A-Z]{3}\d{3}$',patente):
            for camion in lista_camiones:
                if camion._patente == patente:
                    return True
            return False
        else:
            return False
    except Exception as e:
            print(f"Error al validar patente: {e}")

def buscar_camion(patente):
    try:
        for camion in lista_camiones:
            if camion._patente == patente:
                return camion
    except Exception as e:
            print(f"Error al buscar camion: {e}")



##INICIO PROGRAMA
while True:
    print("\nSeleccione la patente del camion que desea evaluar:")
    for camion in lista_camiones:
        print(f"P:[{camion._patente}]", end=' ')
    patente_seleccionada = input("\nCamion?:")
    patente_valid = validar_patente(patente_seleccionada)

    while patente_valid == False: #Vuelvo a solicitar patente si lo ingresado es incorrecto
        print("Patente incorrecta, vuelva a seleccionar:")
        for camion in lista_camiones:
            print(f"P:[{camion._patente}]", end=' ')

        patente_seleccionada = input("\npatente:")
        patente_valid = validar_patente(patente_seleccionada)

    CamionSelected = buscar_camion(patente_seleccionada) #Seteo el camion seleccionado

    opcion = int(input("\n[1] Generar nuevo viaje\n[2] Ver viajes previos\n"))
    while opcion != 1 and opcion != 2:
        print("Indique unicamente opcion 1 o 2")
        opcion = int(input("\n[1] Generar nuevo viaje\n[2] Ver viajes previos\n"))

    if opcion == 1:
        print("\nCiudades disponibles:", end=' ')
        for ciudad in CamionSelected._ciudad_actual._distancias:
            print(f"[{ciudad}] ", end=' ')

        ciudades_select = input("\nIndique las ciudades del recorrido separandolas con una coma:\n")
        ciudades_select = [ciudad.strip() for ciudad in ciudades_select.split(',')]

        CamionSelected.setRecorrido(ciudades_select)
        _estimacion = CamionSelected.estimar_viaje()

        print("\nEstimacion del viaje:\n",_estimacion.detalle())

    elif opcion == 2:
        Estimacion.buscar_estimaciones(CamionSelected._patente)

    input()
    limpiar_terminal()

