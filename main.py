#!/usr/bin/env python3


import subprocess
import os
from datetime import datetime, time


def main():
    print("Iniciando proceso")
    downloads_dir = get_dowload_dir()
    deleteables = scan_dir(downloads_dir)
    if (is_working_time()):
        delete_files(deleteables, True)
    else:
        delete_files(deleteables, False)

    print("finalizado proceso")


def get_dowload_dir():
    '''Metodo apra averiguar llamando al sistema cual es la carpeta de descargas por defeto del sistema'''

    output = subprocess.run(["xdg-user-dir", "DOWNLOAD"], capture_output=True, text=True)
    downloads = ""

    if output.returncode == 0:
        downloads = output.stdout.strip()
    else:
        downloads = "~/Downloads"
      
    print(f"DOWNLOAD DIR: {downloads}")
    return downloads


def scan_dir(downloads_dir):
    '''Escanea el directorio de descargas que es pasado por parametro para localizar 
    todos los archivos que sean de formato .rdp'''
    archivos = os.listdir(downloads_dir)
    rdp_list = []
    for archivo in archivos:
        if str.endswith(archivo, ".rdp"):
            rdp_list.append(os.path.join(downloads_dir, archivo))
            print(f"Agregado archivo {archivo} a la lista de eliminables")

    return rdp_list


def is_working_time():
    '''Calculamos si estamos en periodo de trabajo, si estamos trabajando no eliminamos el ultimo archivo rdp
     ya que podria ser el que necesitemos en el momento'''

    is_working_time = False

    ahora = datetime.now()
    dia_semana = ahora.weekday()
    hora = ahora.time()

    if (dia_semana < 5 and (time(8, 0) <= hora <= time(18, 0))):
        is_working_time = True
    
    return is_working_time


def delete_files(deleteables: list, working_time: bool):
    '''Metodo que itera por los archivos a eliminar y elimina todos o todos menos el ultimo segun
    si estamos fuera de horario laboral, o en horario laboral'''
    deleteables.sort(key=os.path.getmtime, reverse=True)

    if (working_time):
        deleteables = deleteables[1:]
    else:
        deleteables = deleteables
    for file in deleteables:
        try:
            os.remove(file)
            print(f"Archivo eliminado: {file}")
        except FileNotFoundError as e:
            print(f"No se pudo eliminar {file}: {e}")


if __name__ == "__main__":
    main()
