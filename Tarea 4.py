local_1= input("Nombre sucursal 1:")
x_1= int(input("Coordenada x:"))
y_1= int(input("Coordenada y:"))
local_2= input("Nombre sucursal 2:")
x_2= int(input("Coordenada x:"))
y_2= int(input("Coordenada y:"))
local_3= input("Nombre sucursal 3:")
x_3= int(input("Coordenada x:"))
y_3= int(input("Coordenada y:"))
Total=0
contador=0
Total_2=0
flag_orden= True
flag= True
R1=0
R2=0
R3=0
contador_3=1
while flag:
    while flag_orden:
        orden=int(input("Ingrese nùmero del plato:"))
        if orden > 0:
            if orden == 1:
                Total+=4000
            elif orden== 2:
                Total+=3000
            elif orden== 3:
                Total+=3500
        elif orden == -1:
            flag_orden = False
            Total_2+=Total
            print("Total del pedido:$",Total)
            Total= 0


            x_cliente=int(input("Ingrese coordenada x cliente:"))
            y_cliente=int(input("Ingrese coordenada y cliente:"))
            import math
            D1=round(math.sqrt((x_1 - x_cliente)**2 + (y_1 - y_cliente)**2))
            D2=round(math.sqrt((x_2 - x_cliente)**2 + (y_2 - y_cliente)**2))
            D3=round(math.sqrt((x_3 - x_cliente)**2 + (y_3 - y_cliente)**2))
            if D1 < D2 and D1 < D3:
                print("Pedido será entregado por",local_1)
                R1+=1
            elif D2 < D1 and  D2 < D3:
                print("Pedido será entregado por",local_2)
                R2+=1
            elif D3 < D1 and D3 < D2:
                print("Pedido será entregado por",local_3)
                R3+=1
            
            OP=input("¿Desea registrar otro pedido?:")
            if OP == "si":
                flag_orden= True
                contador == 0
            elif OP == "no":
                flag_orden= False
                contador_3= 4
                print("##### Estadísticas Finales #####")
                print("Monto total recaudado $",Total_2)
                print(local_1,"entregó",R1,"pedidos")
                print(local_2,"entregó",R2,"pedidos")
                print(local_3,"entregó",R3,"pedidos")
