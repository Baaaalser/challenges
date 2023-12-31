# /*
#  * Crea un programa que realize el cifrado César de un texto y lo imprima.
#  * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#  *
#  * Te recomiendo que busques información para conocer en profundidad cómo
#  * realizar el cifrado. Esto también forma parte del reto.
#  */

import re

def rotate_list(l, n):
    return l[n:] + l[:n]

def Caesars_cipher(text:str,rot : int,decipher: bool):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    rotated_abc = rotate_list(abc,rot)
    translated = ''

    for word in text:
        filtered = re.search(r"[a-zA-Z]", word, re.MULTILINE)
        if filtered is not None:
            if not decipher:
                translated += rotated_abc[abc.index(filtered[0].lower())]
            else:
                translated += abc[rotated_abc.index(filtered[0].lower())]
        else:
            translated += word
    print(translated)


Caesars_cipher('Ser o no ser, esa es la cuestión.',3,False)
Caesars_cipher('vhu r qr vhu, hvd hv od fxhvwlóq.',3,True)

Caesars_cipher('Ser o no ser, esa es la cuestión.',14,False)
Caesars_cipher('gsf c bc gsf, sgo sg zo qisghwób.',14,True)


