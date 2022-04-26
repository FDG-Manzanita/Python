def obtener_valor_característica(características, buscada):
    cont=0
    for i in características:
        if i[0] == buscada:
            return i[1]
        else:
            cont+=1
    if cont==len(características):
        return 0

def puntaje_amigo(amigo, características):
    suma=0
    for a in amigo[1]:
        o= obtener_valor_característica(características,a)
        suma+=o
    return (suma)


características = [('kawaii',10),('leal',20),('acusete',-10),
('avaro',-15),('respetuoso',20),('otaku',25),
('lolero',25),('furro',-50),('vtuver',25),
('mechero',-30)]

amigos = [('Mojojojo',('mechero','kawaii','furro','lolero')),
('Otaku-taku',('otaku','avaro','lolero','leal')),
('Maiga',('paciente','otaku','leal')), 
('Seiya',('leal','acusete')),
('Vegeta',('otaku','avaro')),
('Sneki',('leal','kawaii','vtuver')),
('Kalila',('lolero','kawaii')),
('Grogu',('avaro','kawaii','lolero','otaku')),
('Freezer',('acusete','furro','otaku','lolero'))]


equipo=[]
for f in amigos:
    nota_amigo= puntaje_amigo(f,características)
    for b in f[1]:
        if b=="lolero":
            equipo.append([nota_amigo,f[0]])
equipo.sort()
equipo.reverse()
cont=0
i=0
print("Equipo seleccionado:")
while cont < 2:
    print(equipo[i][1],",",equipo[i][0],"puntos")
    cont+=1
    i+=1

'''
print(obtener_valor_característica(características, "vtuver"))
print(obtener_valor_característica(características, "puntual"))
print(puntaje_amigo(('Vegeta',('otaku','avaro')), características))
'''