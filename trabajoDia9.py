import os
import re
import datetime
import time
import math


def verificar_cadena_en_archivos(directorio):
    # Definir el patrón de expresión regular
    patron = r'N.{3}-\d{5}'
    contador = 0
    # Recorrer todos los archivos en el directorio
    for base, directorio, archivo in os.walk(directorio):
        for nombre_archivo in archivo:
            ruta_archivo = os.path.join(base,nombre_archivo)
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                coincidencia = re.search(patron,contenido)
                if coincidencia:
                    contador += 1
                    print(f'{nombre_archivo}\t{coincidencia.group()}')
    print(f'\nSe encontraron {contador} coincidencias')


def principal():
    inicio = time.time()
    print('-'* 52)
    print(f'Fecha de busqueda: {datetime.date.today()}\n')
    print('ARCHIVO\t\t\tNro de Serie')
    directorio = 'C:\\Users\\Ferna\\PycharmProjects\\cursoUdemy\\dia9\\Mi_Gran_Directorio\\'
    verificar_cadena_en_archivos(directorio)
    final = time.time()
    print(f'Duracion de la busqueda {math.ceil(final - inicio)} segundos')
    print('-' * 52)


principal()


