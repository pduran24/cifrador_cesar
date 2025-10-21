

from cifrador_cesar import cifrar_mensaje
from txt_edit import escribir_archivo
def descifrar_mensaje(mensaje_cifrado):

    for i in range (1,27):
        mensaje_descifrado = cifrar_mensaje(mensaje_cifrado, -i)
        escribir_archivo("mensajes_posibles.txt", mensaje_descifrado)