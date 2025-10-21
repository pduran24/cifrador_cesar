
from txt_edit import leer_archivo, escribir_archivo
from cifrador_cesar import cifrar_mensaje
from descifrador import descifrar_mensaje

ok,mensaje = leer_archivo("mensaje.txt")

if ok:
    print(mensaje)

    mensaje_cifrado = cifrar_mensaje(mensaje, 3)

    archivo_cifrazo = "mensaje_cifrazo.txt"
    escribir_archivo(archivo_cifrazo, mensaje_cifrado)

    print(f"Mensaje cifrado en archivo {archivo_cifrazo}")

    descifrar_mensaje(mensaje_cifrado)

else:
    print(mensaje)


