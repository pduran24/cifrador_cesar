


def leer_archivo(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            mensaje_original = f.read()
        return True, mensaje_original

    except FileNotFoundError:
        return False, "Archivo no encontrado"
    
def escribir_archivo(archivo, contenido):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(contenido)
        return True
    except Exception as e:
        return False


        
    

        
    