def avistamientos_por_región(nombre_archivo):
    archivo= open(nombre_archivo)
    archivo.readline()
    d={}
#AQUI PARTE TODO Y SEPARO EL ARCHIVO EN LINEAS QUE LUEGO LAS SEPARO EN VARIABLES
    for linea in archivo:
        valores = linea.strip( ).split(';')
        fecha=valores[0].split('-')
        mes=fecha[1]
        año=fecha[0]
        region=valores[1]
        informados=int(valores[2])
        ovnis=int(valores[3])
        promedio= round((ovnis*100)/informados,2)
#ESTO ES PARA CREAR UN DICCIONARIO CON LA LLEVE DE LA REGION Y VALORES DE LAS VARIABLES

        if region not in d:
            d[region]=[]
        if region in d:
            d[region].append((promedio, mes, año, informados))
    for k in d:
        olist=d[k]
        olist.sort()
        olist.reverse()
#AQUI ES TODO DE LA CREACION DE LOS ARCHIVOS POR REGIONES Y LAS ESCRITURAS A LOS MISMOS
        for p, m, a, i in d[k][:3]:
            recu=open("{}.txt".format(k),'a')
            s=("En el mes {} de {} hubo {}% de avistamientos confirmados de un total de {}\n")
            recu.write(s.format(m, a, p, i))
            recu.close()
#UN CONTADOR PARA CACHAR CUANNTAS REGIONES ERAN Y POR ENDE CUANTOS ARCHIVOS SE CREARON  
    contador=len(d)
    archivo.close()
                           
    return (contador)
        
