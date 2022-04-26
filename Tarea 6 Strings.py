def definicion (Parametro_1):
    conter=""
    suma=""
    for caracter in Parametro_1:
        if caracter=="*":
            suma=conter
            conter=""
        else:
            conter+=caracter
    return conter

def emoji(Parametro_1):
    conter=""
    suma=""
    for caracter in Parametro_1:
        if caracter=="*":
            suma==conter
            return conter
        else:
            conter += caracter


def traduccion(Parametro_1,Parametro_2,Parametro_3):
    p=""
    for caracter in Parametro_3:
        p+= caracter
        if p[-len(Parametro_1):]==Parametro_1:
            p=p[:-len(Parametro_1)]
            p+=Parametro_2
    return p




texto=input("Ingrese texto: ")
significado=input("Ingrese significados: ")
conter =""
for caracter in significado:
    if caracter=="$":
        emoji_f= emoji(conter)
        definicion_f=definicion(conter)
        texto=traduccion(emoji_f,definicion_f.upper(),texto)
        conter=""
    else:
        conter+=caracter

print(texto)


#Hola <3, cómo estás? :-D
#<3*corazon$:-D*cara feliz$

#>:( Por qué no me funciona la tarea?!! :´(
#:´(*llanto$>:(*rabia$

#<3 Hola <3 todo el mundo ^.^,bienvenidos a programacion 8-) :P
#8-)*lentes$^.^*emocionada$:P*sacar la lengua$