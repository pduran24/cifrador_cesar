
from txt_edit import leer_archivo, escribir_archivo
from cifrador_cesar import cifrar_mensaje
from descifrador import descifrar_mensaje

ok,mensaje = leer_archivo("mensaje.txt")

ARCHIVO_CIFRADO = "mensaje_cifrado.txt"
ARCHIVO_RESUELTO = "mensaje_descifrado.txt"

if ok:
    mensaje_cifrado = cifrar_mensaje(mensaje, 3)


    if (escribir_archivo(ARCHIVO_CIFRADO, mensaje_cifrado)):
        print(f"Mensaje cifrado en archivo {ARCHIVO_CIFRADO}")

    frase_resuelta, clave, puntuacion = descifrar_mensaje(mensaje_cifrado)

    print(f"Clave probable = {clave}")
    print(f"Confianza = {puntuacion}")
    print(f"Mensaje: {frase_resuelta}")

     
    if (escribir_archivo(ARCHIVO_RESUELTO,frase_resuelta)):
        print(f"Frase resuelta en {ARCHIVO_RESUELTO}")
    

    

else:
    print(mensaje)



