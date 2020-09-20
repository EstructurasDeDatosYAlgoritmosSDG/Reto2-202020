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
import csv
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de peliculas
# -----------------------------------------------------

def loadCSVFile (file, tipo_lista, cmpfunction=None, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    if tipo_lista == 1:
        lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    elif tipo_lista == 2:
        lst = lt.newList("SINGLE_LINKED") #Usando implementacion single linked
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución",t1_stop-t1_start,"segundos")
    return lst

def nuevo_catalogo(details: list, casting: list):
    catalogo = {"productoras": mapa_productoras(details),
                "directores": mapa_directores(casting, details)}
    return catalogo

# ==============================
# Funciones para agregar informacion al catalogo
# ==============================

def mapa_productoras(lista: list):
    tamanio_lista = lista['size']
    mapa_productoras = mp.newMap(numelements=tamanio_lista,maptype='PROBING',loadfactor=0.5, comparefunction=comparar_productoras)
    i = 1
    while i <= tamanio_lista:
        pelicula = lt.getElement(lista, i)
        productora = pelicula['production_companies']
        nombre_pelicula = pelicula['original_title']
        vote_average = pelicula['vote_average']
        existe_productora = mp.contains(mapa_productoras, productora)
        tupla = nombre_pelicula, vote_average
        if not existe_productora:
            lista_pelicula = lt.newList(datastructure='SINGLE_LINKED')
            mp.put(mapa_productoras,productora,lista_pelicula)
        entrada = mp.get(mapa_productoras, productora)
        lt.addLast(entrada['value'], tupla)
        i += 1
    return mapa_productoras

def mapa_directores(casting: list, details: list):
    # Esta funcion hace el mapa de los directores
    tamanio_casting = casting['size']
    mapa_directores = mp.newMap(numelements=tamanio_casting,maptype='PROBING',loadfactor=0.5, comparefunction=comparar_directores)
    tamanio_details = details['size']
    i = 1
    while i <= tamanio_details:
        pelicula_casting = lt.getElement(casting, i)
        pelicula_details = lt.getElement(details, i)
        director = pelicula_casting['director_name']
        id_casting = pelicula_casting['id']
        id_details = pelicula_details['\ufeffid']
        vote_average = pelicula_details['vote_average']
        nombre_pelicula = pelicula_details['original_title']
        tupla = nombre_pelicula, vote_average
        if id_casting != id_details:
            print('Super error')
        existe_director = mp.contains(mapa_directores, director)
        if not existe_director:
            lista_director = lt.newList(datastructure='SINGLE_LINKED')
            mp.put(mapa_directores,director,lista_director)
        entrada = mp.get(mapa_directores, director)
        lista = entrada['value']
        lt.addLast(lista, tupla)
        mp.put(mapa_directores, director, lista)
        i += 1
    return mapa_directores

# ==============================
# Funciones de consulta
# ==============================

def descubrir_productoras(mapa, productora: str) -> tuple:
    entrada = mp.get(mapa, productora)
    lista_peliculas = entrada['value']
    total_peliculas = lt.size(entrada['value'])
    peliculas = lt.newList(datastructure='ARRAY_LIST')
    i = 1
    suma = 0
    while i <= total_peliculas:
        pelicula = lt.getElement(lista_peliculas, i)
        nombre_pelicula = pelicula[0]
        lt.addLast(peliculas, nombre_pelicula)
        vote_average = float(pelicula[1])
        suma += vote_average
        i += 1
    promedio = round(suma/total_peliculas, 2)
    return peliculas, total_peliculas, promedio

def descubrir_director(mapa, director: str) -> tuple:
    entrada = mp.get(mapa, director)
    lista_peliculas = entrada['value']
    total_peliculas = lt.size(entrada['value'])
    peliculas = lt.newList(datastructure='ARRAY_LIST')
    i = 1
    suma = 0
    while i <= total_peliculas:
        pelicula = lt.getElement(lista_peliculas, i)
        nombre_pelicula = pelicula[0]
        lt.addLast(peliculas, nombre_pelicula)
        vote_average = float(pelicula[1])
        suma += vote_average
        i += 1
    promedio = round(suma/total_peliculas, 2)
    return peliculas, total_peliculas, promedio

# ==============================
# Funciones de Comparacion
# ==============================

def comparar_productoras(keyname, author):
    """
    Compara dos productoras. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def comparar_directores(keyname, author):
    """
    Compara dos productoras. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
