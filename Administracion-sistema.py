import os # nos permite interacturar con el sistema operativo
import subprocess # lo mismo pero más eficiente


#os.system("ls") # ejecutar comando para listar recibiendo un string

subprocess.run(["ls","-l","README.md"]) # ejecutar comando recibiendo una lista

"""
Recuperación del sistema
"""

command="uname"
commandArgument="-a"
print(f'Trayendo la información del sistema con el comando: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Recuperando información del disco

command="ps"
commandArgument="-x"
# Imprimir qué es lo que vamos a ejecutar
print(f'Trayendo la información de los procesos activos con el comando: {command} {commandArgument}')

subprocess.run([command,commandArgument])
