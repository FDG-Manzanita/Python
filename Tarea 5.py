def Media_Aritmetica (n1,n2,n3) :
    ResultadoMA= (n1+n2+n3)/3
    ResultadoMA= round(ResultadoMA)
    return ResultadoMA

def Media_Geometrica (n1,n2,n3) :
    ResultadoMG= (n1*n2*n3)**(1/3)
    ResultadoMG=round(ResultadoMG)
    return ResultadoMG

def Media_Vuelta (n1,n2,n3) :
    ResultadoMV= ((n3*((Media_Aritmetica(n1, n2, n3))**2))**(1/3))
    ResultadoMV = round(ResultadoMV)
    return ResultadoMV

def Opciones_de_pasar (nf_aritmetica,nf_geometrica,nf_vuelta) : 
    if nf_aritmetica<55 and nf_geometrica<55 and nf_vuelta<55:
        resultado=0
    elif nf_aritmetica>=55 and nf_geometrica<55 and nf_vuelta<55:
        resultado=1
    elif nf_aritmetica<55 and nf_geometrica>=55 and nf_vuelta<55:
        resultado=2
    elif nf_aritmetica<55 and nf_geometrica<55 and nf_vuelta>=55:
        resultado=3 
    elif nf_aritmetica>=55 and nf_geometrica>=55 and nf_vuelta<55:
        resultado=2
    elif nf_aritmetica>=55 and nf_geometrica<55 and nf_vuelta>=55:
        resultado=1
    elif nf_aritmetica<55 and nf_geometrica>=55 and nf_vuelta>=55:
        resultado=3 
    elif nf_aritmetica>=55 and nf_geometrica>=55 and nf_vuelta>=55:
        resultado=1
    return resultado




pedir_notas = True
while pedir_notas:
    ramo = input("Ingrese el nombre del ramo: ")

    if ramo == "salir":
        pedir_notas = False
        print("Fin del programa - Desarrollado por Kiwi :D!")
    else:
        n1 = int(input("Ingrese la 1era nota: "))
        n2 = int(input("Ingrese la 2era nota: "))
        n3 = int(input("Ingrese la 3era nota: "))

        nf_aritmetica = (Media_Aritmetica(n1, n2, n3)) # Aquí debes llamar a la función que calcula la NF con Media Aritmética
        nf_geometrica = (Media_Geometrica(n1, n2, n3)) # Aquí debes llamar a la función que calcula la NF con Media Geométrica
        nf_vuelta = (Media_Vuelta(n1, n2, n3)) # Aquí debes llamar a la función que calcula la NF con Media Vuelta

        print("Su nota final según la Media Aritmética es:", nf_aritmetica)
        print("Su nota final según la Media Geométrica es:", nf_geometrica)
        print("Su nota final según la Media Vuelta es:", nf_vuelta)

        nf_aprobacion = (Opciones_de_pasar(nf_aritmetica, nf_geometrica, nf_vuelta)) # Aquí debes llamar a la función que revisa con qué fórmula se aprueba

        if nf_aprobacion == 0:
            print("Lamentablemente no puedes aprobar con ninguna de las fórmulas :'c")
        elif nf_aprobacion == 1:
            print("Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 2:
            print("Si la NF del ramo se calcula usando la Media Geométrica, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 3:
            print("Si la NF del ramo se calcula usando la Media Vuelta, entonces apruebas", ramo, ":D")
