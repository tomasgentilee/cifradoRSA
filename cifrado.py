from Crypto.Util.number import inverse, GCD
import gc

"""

Valores recomendados para p y q:
p = 61
q = 53
Estos valores son ambos números primos y son comúnmente utilizados en ejemplos y ejercicios de RSA debido a su tamaño manejable y a que su 
producto (p * q) es suficientemente grande para proporcionar seguridad.

Valor para recomendado para e:
e = 65537
El valor de e suele ser un número primo relativamente pequeño y comúnmente se utiliza el valor 65537 en la práctica, ya que tiene 
buenas propiedades para el cifrado RSA.

"""

def generar_claves_rsa():

    p = int(input("Ingrese un numero primo p: "))
    q = int(input("Ingrese un numero primo q: "))
    e = int(input("Ingrese un numero entero positivo impar e que cumpla la condición siguiente: mcd(e, φ) = 1.: "))
    print("Matemáticamente, esta condición sirve para obtener un valor e que se considera co-primo, o sea relativamente primo, de N’.")
    N = p * q
    
    print(f"Mediante p * q obtenemos N, el cual vale {N}.  N es el módulo para ambas claves, pública y privada.")

    print(" ")

    φ = (p - 1) * (q - 1)
    print(f"Luego realizamos (p- 1) * (q - 1) para obtener N' o tambien llamado φ(N), el cual vale {φ}. Esta es la función de Euler")

    if GCD(e, φ) != 1:
        raise ValueError("e no es co-primo con φ(N). Elige otro valor de e.")

    print(" ")
    d = inverse(e, φ)
    print(f"Calcular d como el inverso multiplicativo de e módulo φ(N), el cual nos da d = {d}")

    print(" ")

    print(f"Clave pública (e, N): ({e}, {N})")
    clave_publica = (e, N)
    print(f"Clave privada (d, N): ({d}, {N})")
    clave_privada = (d, N)

    print(" ")
    cifrado = cifrar_mensaje(clave_publica)

    print(f"El mensaje cifrado es {cifrado}")

    print(" ")
    descifrado = descifrar_mensaje(cifrado, clave_privada)

    print(f"El mensaje descifrado es {descifrado}")
    print(" ")


def cifrar_mensaje(clave_publica):

    print("Para el cifrado del mensaje m se utiliza la clave publica (e, N)")

    """
    Convertimos el mensaje a números usando el código ASCII
    Utilizando el código ASCII se expresa el mensaje m en un número M
    """
    
    mensaje = input("Ingrese el mensaje a cifrar: ")

    numeros_mensaje = [ord(caracter) for caracter in mensaje]

    print(f"Convertimos el mensaje a su correspondiente valor ASCII: {numeros_mensaje}")

    e, N = clave_publica

    print(f"Tomamos los valores de la clave publica, los cuales son e = {e} y N = {N}")

    cifrado = [pow(num, e, N) for num in numeros_mensaje]

    print(f"Ciframos cada numero del mensaje obteniendo el mensaje cifrado: {cifrado}. Se obtiene el mensaje cifrado C calculando C = M^e mod N.")

    return cifrado

def descifrar_mensaje(cifrado, clave_privada):
    
    print("Para descifrar el mensaje cifrado C se utiliza la clave privada (d, N)")

    d, N = clave_privada

    print(f"Tomamos los valores de la clave privada, los cuales son d = {d} y N = {N}, como tambien el mensaje cifrado {cifrado}")

    descifrado = [pow(num, d, N) for num in cifrado]

    print("Desciframos cada numero del mensaje cifrado. Se obtiene el mensaje descifrado M calculando M = C^d mod N. En caso de tener letras el M obtenido es la representación numérica en ASCII del mensaje original m.")

    mensaje_descifrado = ''.join(chr(num) for num in descifrado)

    return mensaje_descifrado

    

if '__main__':
    generar_claves_rsa()