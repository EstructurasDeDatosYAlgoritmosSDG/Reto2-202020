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
archivo_AllMoviesDetailsCleaned = 'Data/themoviesdb/AllMoviesDetailsCleaned.csv'
archivo_smallmoviesdetailscleaned = 'Data/themoviesdb/SmallMoviesDetailsCleaned.csv'
archivo_allmoviescastingraw = 'Data/themoviesdb/AllMoviesCastingRaw.csv'
archivo_moviescastingraw_small = 'Data/themoviesdb/MoviesCastingRaw-small.csv'

# ___________________________________________________
#  Funciones para imprimir la información de
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
    print('4- Conocer a un director')
    print('5- Conocer a un actor')
    print('6- Entender un género cinematográfico')
    print('7- Encontrar películas por país')
    print("0- Salir")

def main():
    details = ''
    casting = ''
    catalogo = ''

    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:

            details = controller.loadCSVFile(archivo_AllMoviesDetailsCleaned, 1)
            casting = controller.loadCSVFile(archivo_allmoviescastingraw, 1)
            datos = controller.infoArchivoCsv(details)
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
            catalogo = controller.cargar_catalogo(details, casting)
            print('El catálogo se cargó correctamente. :)\n')
            t1_stop = process_time() #tiempo final
            print("Tiempo de ejecución",t1_stop-t1_start,"segundos\n")

        elif  int(inputs[0]) == 3:
            t1_start = process_time() #tiempo inicial
            productora = input('Ingrese el nombre de la compañia de producción: \n')
            datos = controller.infoProductora(catalogo['productoras'],productora)
            print('\nLa lista de películas producidas por la productora',productora,'es:\n')
            i = 1
            while i <= datos[1]:
                pelicula = lt.getElement(datos[0], i)
                print(pelicula)
                i += 1
            print('\nLa cantidad de películas producidas por',productora,'es de:', datos[1])
            print('\nLa calificación promedio de las películas de la productora', productora, 'es de:',datos[2], '\n')
            t1_stop = process_time() #tiempo final
            print("Tiempo de ejecución",t1_stop-t1_start,"segundos\n")

        elif  int(inputs[0]) == 4:
            t1_start = process_time() #tiempo inicial
            director = input('Ingrese el nombre del director: \n')
            datos = controller.infoDirector(catalogo['directores'],director)
            print('\nLa lista de películas producidas por el director',director,'es:\n')
            i = 1
            while i <= datos[1]:
                pelicula = lt.getElement(datos[0], i)
                print(pelicula)
                i += 1
            print('\nLa cantidad de películas producidas por',director,'es de:', datos[1])
            print('\nLa calificación promedio de las películas del director', director, 'es de:',datos[2], '\n')
            t1_stop = process_time() #tiempo final
            print("Tiempo de ejecución",t1_stop-t1_start,"segundos\n")

        elif int(inputs[0]) == 5:
            t1_start = process_time() #tiempo inicial
            actor= input('Ingrese el nombre del actor: \n')
            datos= controller.infoActores(catalogo['actores'],actor)
            print('\nLa lista de películas en la que actuó ', actor,'es: \n')
            i=1
            while i < datos[1]:
                pelicula= lt.getElement(datos[1],i)
                print(pelicula)
                i+=1
            print('\nLa cantidad de películas en las que actuó es de: ', datos[3])
            print('\nEl director con el que más trabajó fue:', datos[2])
            t1_stop = process_time() #tiempo final
            print("Tiempo de ejecución",t1_stop-t1_start,"segundos\n")
            
        elif  int(inputs[0]) == 6:
            t1_start = process_time() #tiempo inicial
            genero = input('Ingrese el género cinematográfico: \n')
            datos = controller.infoGenero(catalogo['generos'], genero)
            print('La lista de todas las películas asociadas al género', genero, 'es:')
            i = 1
            while i <= datos[1]:
                pelicula = lt.getElement(datos[0], i)
                print(pelicula)
                i += 1
            print('\nEl total de películas del género', genero, 'es de:', datos[1])
            print('\nEl promedio de votos de las películas del género', genero, 'es de:', datos[2], '\n')
            t1_stop = process_time() #tiempo final
            print("Tiempo de ejecución",t1_stop-t1_start,"segundos\n")
        
        elif  int(inputs[0]) == 7:
            t1_start = process_time() #tiempo inicial
            pais = input('Ingrese el nombre del país de producción: \n')
            datos = controller.infoPais(catalogo['paises'],pais)
            print('\nLa lista de películas producidas en el país',pais,'es:\n')
            i = 1
            while i <= datos[1]:
                pelicula = lt.getElement(datos[0], i)
                print('El nombre de la película es:', pelicula[0], '\nLa fecha de producción es:', pelicula[1], '\nEl productor de la película es:', pelicula[2],'\n')
                i += 1
            t1_stop = process_time() #tiempo final
            print("Tiempo de ejecución",t1_stop-t1_start,"segundos\n")



        else:
            sys.exit(0)
    sys.exit(0)
    

if __name__ == "__main__":
    main()

