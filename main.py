import subprocess
import os
from datetime import datetime, time


def main():
    print("Iniciando proceso")
    downloads_dir = get_dowload_dir()
    scan_dir(downloads_dir)

    if (is_working_time()):
        delete_working_time()
    else:
        delete_No_working()

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
    archivos = os.listdir(downloads_dir)
    rdp_list = []
    for archivo in archivos:
        if str.endswith(archivo, ".rdp"):
            rdp_list.append(archivo)


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


def delete_working_time():
    return None


def delete_No_working():
    return None


if __name__ == "__main__":
    main()
