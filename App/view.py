"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
from time import process_time 

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import map as mp
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________





# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("Bienvenido")
    print("1- Información archivo cargado")
    print("2- Cargar catálogo")
    print('3- Conocer compañia de producción')
    print("0- Salir")

def main():
    lista = ''
    catalogo = ''

    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            lista = controller.loadCSVFile('Data/themoviesdb/AllMoviesDetailsCleaned.csv', 1)
            datos = controller.infoArchivoCsv(lista)
            print('El número de películas cargadas es:', datos[0],'\n')
            print('Primera película:\n')
            print('Título:', datos[1][0])
            print('Fecha de estreno:',datos[1][1])
            print('Promedio de votación:',datos[1][2])
            print('Número de votos:',datos[1][3])
            print('Idioma:',datos[1][4],'\n')
            print('Última película:\n')
            print('Título:', datos[2][0])
            print('Fecha de estreno:',datos[2][1])
            print('Promedio de votación:',datos[2][2])
            print('Número de votos:',datos[2][3])
            print('Idioma:',datos[2][4],'\n')
        
        elif  int(inputs[0]) == 2:
            t1_start = process_time() #tiempo inicial
            catalogo = controller.cargar_catalogo(lista)
            print('El catálogo se cargó correctamente. :)\n')
            t1_stop = process_time() #tiempo final
            print("Tiempo de ejecución",t1_stop-t1_start,"segundos\n")

        elif  int(inputs[0]) == 3:
            t1_start = process_time() #tiempo inicial
            productora = input('Ingrese el nombre de la compañia de producción: \n')
            datos = controller.infoProductora(catalogo['productoras'],productora)
            print('La lista de películas producidas por la productora',productora,'es:')
            i = 1
            while i <= datos[1]:
                pelicula = lt.getElement(datos[0], i)
                print(pelicula)
                i += 1
            print('\nLa cantidad de películas producidas por',productora,'es de:', datos[1])
            print('\nLa calificación promedio de las películas de la productora', productora, 'es de:',datos[2], '\n')
            t1_stop = process_time() #tiempo final
            print("Tiempo de ejecución",t1_stop-t1_start,"segundos\n")

        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    main()