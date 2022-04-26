def obtener_valor_característica(características, buscada):
    cont=0
    conter=0
    while conter< len(características):
        nombre, puntaje=características[conter]
        if nombre == buscada:
            return puntaje
        else:
            conter+=1
            cont+=1
    if cont==len(características):
        return 0

def puntaje_amigo(amigo, características):
    s=0
    nombre, caracter =amigo
    for a in caracter:
        valor_sumado_de_caracteristicas= obtener_valor_característica(características,a)
        s+=valor_sumado_de_caracteristicas
    return (s)


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




print(obtener_valor_característica(características, "vtuver"))
print(puntaje_amigo(('Vegeta',('otaku','avaro')), características))
