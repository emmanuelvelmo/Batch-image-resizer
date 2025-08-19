import pathlib # Manejo moderno de rutas de archivos y directorios
import cv2 # OpenCV: lectura de imágenes

# VARIABLES
extensiones_lista = ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'webp', 'gif', 'heic'] # Lista de formatos de imagen soportados por OpenCV
lado_minimo = 0
ancho_val = 
alto_val = 

# Determinar el lado menor
if ancho_val < alto_val:
  lado_minimo = ancho_val
else:
  lado_minimo = alto_val

# FUNCIONES



# PUNTO DE PARTIDA
# Bucle principal del programa
    while True:
        # Solicitar directorio de entrada
        while True:
            directorio_entrada = input("Enter directory: ").strip('"\'')
            
            # Verificar que el directorio exista
            if not pathlib.Path(directorio_entrada).exists():
                print("Wrong directory\n")
            else:
                break
        
        # Solicitar lado mínimo de imagen
        while True:
            valor_usuario = input("Enter minimum size for width or height: ")
            
            # Únicamente número
            if valor_usuario != :
                print("Wrong format\n")
            else:
                break
        
        # Establecer nuevo ancho y alto para imagen de salida
        ancho_val = round(ancho_val * (valor_usuario / lado_minimo))
        alto_val = round(alto_val * (valor_usuario / lado_minimo))
        
        
        
        
        
        
