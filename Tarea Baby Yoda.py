#Tarea Del Bebe Yoda xd
#Primero le pedimos al usuario que ingrese una cantidad de Nevarru Nimmies,Space Soup y Carne de Rana que consumio grogu
nn = float(input( "Nevarru Nimmies consumidas (en unidades):"))
ss = float(input( "Space Soup consumidas (en ml):"))
cr = float(input( "Carne de rana consumida (en gramos):"))
#Aqui se empieza a hacer los calculos matematicos correspondientes,para sacar la cantidad de grasa,carbohdratos y proteinas del Nevarru Nimmies (nn)
GN = nn*1.90
CN = nn*6.00
PN = nn*0.80
#Aqui se empieza a hacer los calculos matematicos correspondientes,para sacar la cantidad de grasa,carbohdratos y proteinas de la Space Soup (ss)
GS = ss/285 * 10.00
CS = ss/285 * 12.00
PS = ss/285 * 11.00
#Aqui se empieza a hacer los calculos matematicos correspondientes,para sacar la cantidad de grasa,carbohdratos y proteinas de la Carne de Rana (cr)
GC = cr/100 * 0.30
CC = cr/100 * 0.00
PC = cr/100 * 16.0
#ahora una suma acumulada para saber cuanta grasa,proteina y carbohidratos consumio en total
GN +=GS+GC
CN +=CS+CC
PN +=PS+PC
#Aqui se redondea a 2 decimales
GN= round(GN,2)
CN= round(CN,2)
PN= round(PN,2)
#Aqui se hace la tansformacion de grasa,carbohidratos y proteinas a calorias 
CAL= (GN*9)+(CN*4)+(PN*4)
CAL= round(CAL)
#Para termiar se coloca el mensaje al usuario con los datos
print("Grogu ha consumido:")
print(GN,"[g] de grasas")
print(CN,"[g] de carbohidratos")
print(PN,"[g] de proteinas")
print("Dando un total de:",CAL,"[calorias]")
#EJ1 Nevarru Nimmies:5 Space soup:250 Carne de rana:170
#Grogu ha consumido:
#18.78 [g] de grasas
#40.53 [g] de carbohidratos
#40.85 [g] de proteinas
#Dando un total de: 495 [calorias]

#EJ2 Nevarru Nimmies:3 Space Soup:840 Carne de rana:420
#Grogu ha consumido:
#36.43 [g] de grasas
#53.37 [g] de carbohidratos
#102.02 [g] de proteinas
#Dando un total de: 949 [calorias]

#EJ3 Nevarru Nimmies:10 Space soup 300 Carne de rana:500
#Grogu ha consumido:
#31.03 [g] de grasas
#72.63 [g] de carbohidratos
#99.58 [g] de proteinas
#Dando un total de: 968 [calorias]
