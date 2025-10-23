

def leer_diccionario(archivo="wordlist.txt"):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            palabras = f.read().lower().splitlines()

            return set(palabras)
    except FileNotFoundError:
        print("Archivo no encontrado")
        return None
    except Exception as e:
        print("Error al leer el diccionario")
        return None


def puntuar_frase(frase, diccionario_valido):
    puntuacion = 0
    palabras = frase.lower().split()

    if not palabras:
        return 0
    
    for palabra in palabras:
        palabra_limpia = palabra.strip(".,;:?!")

        if palabra_limpia in diccionario_valido:
            puntuacion += 1

    return round(puntuacion/len(palabras), 2)