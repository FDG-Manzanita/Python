def verificacion (dosis,rut):
    if rut not in dosis:
        return 0
    else:
        return 1
def ingreso_vacuna(vacunas,tipo,rut):
    if tipo in vacunas:
        vacunas[tipo].append(rut)
    elif tipo not in vacunas:
        vacunas[tipo]=[]
        vacunas[tipo].append(rut)
    return
def ingreso_dosis (dosis,rut,edad,fecha):
    dosis[rut]=[edad,fecha]
    return
def vsegunda(dosis,rut):
    if len(dosis[rut]) == 3:
        return 1
    else:
        return 0
def accion_1(dosis,fecha,rut):
    dosis[rut].append(fecha)
    return
def investigacion_de_tipos(vacunas,rut):
    for llave in vacunas:
        if rut in vacunas[llave]:
            return llave
def mayores(dosis):
    nueva=[]
    for llave in dosis:
        a=vsegunda(dosis,llave)
        if a == 1:
            nueva.append(int(dosis[llave][0]))
    return nueva
def ultima(mayor):
    dic = {}
    for a in mayor:
        if a not in dic:
            dic[a] = 0
        dic[a] += 1
    return dic
def orden(l):
    l.sort()
    l.reverse()
    return l
#PUEDE QUE PAREZCAN MUCHAS FUNCIONES Y SI LO SON PERO CADA UNA ES PARA EVITAR ENREDARME EN EL CODIGO PRINCIPAL Y PODER HACER
#LAS OPERACIONES NECESARIAS 

#EDITABLE
vacunas = {
"Sinovac":["11.111.111-1", "12.345.678-9","6.123.456-7"],
"Pfizer": ["8.978.657-3"],
"CanSino": ["13.789.456-k"],
"Astra Zeneca": ["29.987.654-3","12.345.111-1"]
}
#ESTO ES TOTAL MENTE EDITABLE
dosis = {
"11.111.111-1":[55,(2021,4,11),(2021,5,10)],
"12.345.678-9":[47,(2021,6,3),(2021,6,17)],
"8.978.657-3":[79,(2021,3,23)],
"13.789.456-k":[40,(2021,5,18),(2021,6,10)],
"29.987.654-3":[40,(2021,6,17),(2021,6,17)],
"6.123.456-7": [79,(2021,6,3),(2021,6,23)],
"12.345.111-1":[79,(2021,6,3)]
}

flag=True
dia=input("Ingrese Día:")
mes=input("Ingrese Mes:")
año=input("Ingrese Año:")
fecha=(año,mes,dia)
#AQUI HAY UN WHILE PARA COLOCAR EL RUT O PRINTEAR SI YA NECESITA 2DA DOSIS O SI TERMINO LA INOCULACION
while flag:
    rut=input("Ingrese RUT:")
    esta=verificacion(dosis,rut)
    if esta == 0:
        edad=input("Ingrese Edad:")
        tipo=input("Ingrese tipo de vacuna:")
        fecha=(año,mes,dia)
        ingreso_dosis(dosis,rut,edad,fecha)
        ingreso_vacuna(vacunas,tipo,rut)
    elif esta == 1:
        segunda=vsegunda(dosis,rut)
        if segunda == 0:
            accion_1(dosis,fecha,rut)
            tipo2=investigacion_de_tipos(vacunas,rut) 
            print("Segunda dosis.El paciente debe ser inoculado con:",tipo2)
        elif segunda == 1:
            print ("Ya completó el proceso de inoculacion.")
    continuar=input("¿Desea continuar? (s/n):")
    if continuar == "s":
        flag=True
    elif continuar == "n":
        flag=False
mayor=[]
mayor=mayores(dosis)
mar=orden(mayor)
final=ultima(mar)
cont=0
lista_nueva=[]
for llave in final:
    a=(final[llave],llave)
    lista_nueva.append(a)
lista_nueva.sort()
lista_nueva.reverse()
#PROCESO FINAL DONDE EMPIEZO A PRINTEAR
print("Edades con más personas con esquema de inoculación completo:")
for tupla in lista_nueva:
    personas, edad =tupla
    print(edad,"años:",personas,"personas")
    cont+=1
    if cont == 3:
        break
