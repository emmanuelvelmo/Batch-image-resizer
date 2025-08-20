import pathlib # Manejo moderno de rutas de archivos y directorios
import cv2 # OpenCV: lectura de imágenes

# VARIABLES
extensiones_lista = ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'webp', 'gif', 'heic'] # Lista de formatos de imagen soportados por OpenCV
valor_usuario = 0
directorio_entrada = ""

# FUNCIONES
procesar_directorio_imagenes():
    global extensiones_lista, valor_usuario, directorio_entrada, ancho_val, alto_val

    # Generar nombre para directorio de salida
    directorio_salida = f"{pathlib.Path(directorio_entrada).name} (output)"
    
    # Mostrar separador visual para inicio de resultados
    print("-" * 36)
    
    # Procesar recursivamente cada imagen en el directorio
    for extension_val in extensiones_lista:
        for archivo_iter in pathlib.Path(directorio_entrada).rglob(f'*.{extension_val}'):
            if archivo_iter.is_file():
                # Cargar imagen desde archivo usando OpenCV
                imagen_val = cv2.imread(str(archivo_iter))

                # Capturar dimensiones de la imagen
                ancho_val = cv2.height(imagen_val) #############################################################################
                alto_val = cv2.height(imagen_val) #############################################################################
                
                lado_minimo = 0

                # Determinar el lado menor
                if ancho_val < alto_val:
                  lado_minimo = ancho_val
                else:
                  lado_minimo = alto_val

                # Establecer nuevo ancho y alto para imagen de salida
                ancho_val = round(ancho_val * (valor_usuario / lado_minimo))
                alto_val = round(alto_val * (valor_usuario / lado_minimo))

                # Redimensionar imagen a nuevos valores de ancho y alto
                imagen_val = cv2.() #############################################################################

                # Generar ruta relativa para mantener estructura de directorios
                carpeta_destino = pathlib.Path(directorio_salida) / pathlib.Path(iter_carpeta).relative_to(pathlib.Path(directorio_entrada)) #############################################################################
        
                # Crear carpeta de destino si no existe
                carpeta_destino.mkdir(parents = True, exist_ok = True)

                # Guardar imágen en directorio de salida correspondiente
                cv2.save(imagen_val) #############################################################################

                # Mostrar archivo procesado
                print("directorio/archivo.extension") #############################################################################

    # Mostrar separador final
    print("-" * 36 + "\n")

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
            if valor_usuario != : #############################################################################
                print("Wrong format\n")
            else:
                break
        
        # Procesar directorio de imágenes recursivamente
        procesar_directorio_imagenes()
