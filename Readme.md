🇪🇸 **ESPAÑOL**

# Auto-.RDP-Cleanup

### Script en Python para gestionar archivos de conexión RDP de manera eficiente

Auto-RDP-Cleanup es un script en Python diseñado para facilitar la gestión de archivos de protocolo de escritorio remoto (RDP) generados al conectarse a servidores remotos desde un sistema basado en Linux. Para usuarios que se conectan frecuentemente a escritorios remotos, especialmente en entornos con desconexiones o reconexiones frecuentes, este script automatiza la limpieza de archivos `.rdp`, reduciendo el desorden en la carpeta de descargas.

## Funcionalidades clave
- **Detección automática del directorio de descargas**: El script usa `xdg-user-dir` para detectar la carpeta de descargas predeterminada, lo que lo hace compatible con cualquier sistema Linux.
- **Limpieza inteligente de archivos**: Gestiona los archivos `.rdp` en dos modos:
  - **Modo horario laboral**: Elimina todos los archivos `.rdp` excepto el más reciente, manteniéndolo por si es necesario reconectar.
  - **Modo fuera de horario laboral**: Borra todos los archivos `.rdp`, asumiendo que ya no son necesarios.
- **Fácil integración**: Ideal para quienes usan conexiones RDP frecuentemente y buscan una manera simple de gestionar archivos `.rdp` sin intervención manual.

## Requisitos
- Python 3.x
- Sistema operativo Linux con `xdg-user-dir` instalado (incluido en la mayoría de las distribuciones)

## Instalación
Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tuusuario/auto-rdp-cleanup.git
cd auto-rdp-cleanup
```


🇬🇧 **ENGLISH**

# Auto-.RDP-Cleanup

### Python Script to Manage RDP Connection Files Efficiently

Auto-RDP-Cleanup is a Python script designed to streamline the management of Remote Desktop Protocol (RDP) files generated while connecting to remote servers via RDP on a Linux-based system. For users frequently connecting to remote desktops, especially in environments with frequent disconnections or reconnections, this script automates the cleanup of `.rdp` files, reducing clutter in the downloads folder. 

## Key Features
- **Automatic Download Directory Detection**: The script uses `xdg-user-dir` to detect the user's default downloads folder, making it compatible with any Linux system.
- **Intelligent File Cleanup**: Cleans up `.rdp` files in two modes:
  - **Work Hours Mode**: Deletes all but the most recent `.rdp` file, preserving it for potential reconnections.
  - **Non-Work Hours Mode**: Deletes all `.rdp` files, assuming they are no longer needed.
- **Easy to Integrate**: Ideal for those using RDP connections frequently and looking for a simple way to manage `.rdp` files without manual intervention.

## Requirements
- Python 3.x
- Linux OS with `xdg-user-dir` installed (most distributions include this by default)

## Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/auto-rdp-cleanup.git
cd auto-rdp-cleanup






