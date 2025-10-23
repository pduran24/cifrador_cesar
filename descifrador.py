

from cifrador_cesar import cifrar_mensaje
from diccionario import leer_diccionario, puntuar_frase

def descifrar_mensaje(mensaje_cifrado):

    diccionario = leer_diccionario()

    print("Iniciando analisis...")

    mejor_frase = ""
    max_puntuacion = -1  
    mejor_clave = 0


    for i in range(1,27):
        frase = cifrar_mensaje(mensaje_cifrado, -i)

        puntuacion = puntuar_frase(frase, diccionario)

        if puntuacion > max_puntuacion:
            max_puntuacion = puntuacion
            mejor_frase = frase
            mejor_clave = i
        
    
    return mejor_frase, mejor_clave, max_puntuacion


