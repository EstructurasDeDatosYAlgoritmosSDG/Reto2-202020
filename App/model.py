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

def descubrir_productoras(lista: list, productora: str) -> tuple:
    tamanio_lista = lista['size'] 
    mapa_companias = mp.newMap(tamanio_lista,maptype='CHAINING',loadfactor=1.5)
    i = 1
    while i <= tamanio_lista:
        pelicula = lt.getElement(lista, i)
        productora = pelicula['production_companies']
        if not mp.contains(mapa_companias, productora):
            mapa_compania = mp.newMap(0,maptype='CHAINING',loadfactor=1.5)
            mp.put(mapa_companias, productora, mapa_compania)
        nombre_pelicula = pelicula['original_title']
        vote_average = pelicula['vote_average']
        mp.put(mapa_companias[mapa_compania],nombre_pelicula,vote_average)
        i += 1
    mapa_nombre_peliculas = mp.get(mapa_companias, productora)
    i = 1
    lista_nombres = lt.newList(datastructure='ARRAY_LIST')
    tamanio_mapa_nombre_peliculas = mp.size(mapa_nombre_peliculas)
    suma = 0
    while i <= tamanio_mapa_nombre_peliculas:
        pelicula = mp.get(mapa_nombre_peliculas,i)
        nombre_pelicula = pelicula[0]
        vote_average = pelicula[1]
        lt.addLast(nombre_pelicula)
        suma += vote_average
    promedio = suma / tamanio_mapa_nombre_peliculas
    return lista_nombres, tamanio_mapa_nombre_peliculas, promedio

# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================


