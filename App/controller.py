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

import config as cf
from App import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def loadCSVFile(file, tipo_lista, cmpfunction=None, sep=";"):
    lista = model.loadCSVFile(file, tipo_lista, cmpfunction=None, sep=";")
    return lista

def infoArchivoCsv(lista: list):
    num_peliculas = lista['size']
    #Primera pelicula
    primer_elemento = lt.firstElement(lista)
    titulo_primera = primer_elemento['original_title']
    fecha_primera = primer_elemento['release_date']
    vote_average_primera = primer_elemento['vote_average']
    vote_count_primera = primer_elemento['vote_count']
    language_primera = primer_elemento['original_language']
    primera = [titulo_primera, fecha_primera, vote_average_primera, vote_count_primera, language_primera]
    #Ultima pelicula
    ultimo_elemento = lt.lastElement(lista)
    titulo_ultima = ultimo_elemento['original_title']
    fecha_ultima = ultimo_elemento['release_date']
    vote_average_ultima = ultimo_elemento['vote_average']
    vote_count_ultima = ultimo_elemento['vote_count']
    language_ultima = ultimo_elemento['original_language']
    ultima = [titulo_ultima, fecha_ultima, vote_average_ultima, vote_count_ultima, language_ultima]
    return num_peliculas, primera, ultima





    




# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
