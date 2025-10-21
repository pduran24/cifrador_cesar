
def cifrar_mensaje(texto, desplazamiento):

    ALFABETO_MIN = "abcdefghijklmnñopqrstuvwxyz"
    ALFABETO_MAY = ALFABETO_MIN.upper()

    mensaje_cifrado = ""

    for caracter in texto:

        # se comprueba si es un aletra
        if caracter in ALFABETO_MIN:
            indice_actual = ALFABETO_MIN.find(caracter)
            nuevo_indice = (indice_actual + desplazamiento) % len(ALFABETO_MIN)
            mensaje_cifrado += ALFABETO_MIN[nuevo_indice]
        
        elif caracter in ALFABETO_MAY:
            indice_actual = ALFABETO_MAY.find(caracter)
            nuevo_indice = (indice_actual + desplazamiento) % len(ALFABETO_MAY)
            mensaje_cifrado += ALFABETO_MAY[nuevo_indice]

        else:
            mensaje_cifrado += caracter
    
    return mensaje_cifrado