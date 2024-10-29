import subprocess


def main():
    print("Iniciando proceso")
    downloads_dir = get_dowload_dir()
    scan_dir(downloads_dir)
    print("finalizado proceso")


def get_dowload_dir():
    '''Metodo apra averiguar llamando al sistema cual es la carpeta de descargas por defeto del sistema'''

    output = subprocess.run(["xdg-user-dir", "DOWNLOAD"], capture_output=True, text=True)
    downloads = ""

    if output.returncode == 0:
        downloads = output.stdout
    else:
        downloads = "~/Downloads"
      
    print(f"DOWNLOAD DIR: {downloads}")
    return downloads


def scan_dir(downloads_dir):
    print("scanning")


if __name__ == "__main__":
    main()
