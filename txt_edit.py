


def leer_archivo(archivo):


    try:
        with open(archivo, 'r') as f:
            mensaje_original = f.read()
        return True, mensaje_original

    except FileNotFoundError:
        return False, "Archivo no encontrado"
    

def escribir_archivo(archivo, contenido):

    with open(archivo, 'a') as f:
        f.write(contenido)

        
    

        
    