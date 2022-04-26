Valor= float(input("Inserte el valor en UF (entre 1500 y 13000):"))
if 1500<=Valor<=13000:
    Pie= int(input("Inserte el porcentaje de pie de inicio que le dara (sin el simbolo %)(20-45):"))
    if 20<=Pie<=45:
        Plazo= int(input("Inserte los años de plazo (20-25-30):"))
        if Plazo== 20 or Plazo==25 or Plazo==30:
            Tipo=int(input("Inserte el tipo de vivienda [1] si es casa y [2] si es departamento:"))
            if Tipo==1 or Tipo==2:
                Estado= int(input("Inserte el estado de la vivienda [1] si es nuevo y [2] si es usado:"))
                if Estado==1 or Estado==2:
                    Pie2= float(Pie/100)
                    Valor2= Valor-(Valor*Pie2)
                    if Tipo==1:
                        if Estado==1:
                            if Plazo==20: Valor3 = (Valor2*(25/100))+Valor2
                            elif Plazo==25: Valor3 = (Valor2*(30/100))+Valor2
                            else: Valor3 = (Valor2*(35/100))+Valor2
                        else:
                            if Plazo==20: Valor3 =( Valor2*(22/100))+Valor2
                            elif Plazo==25: Valor3 = (Valor2*(27/100))+Valor2
                            else: Valor3 = (Valor2*(31/100))+Valor2
                    else:
                        if Estado==1:
                            if Plazo==20: Valor3=(Valor2*(28/100))+Valor2
                            elif Plazo==25: Valor3=(Valor2*(33/100))+Valor2
                            else: Valor3=(Valor2*(41/100))+Valor2
                        else:
                            if Plazo==20: Valor3 = (Valor2*(26/100))+Valor2
                            elif Plazo==25: Valor3 = (Valor2*(32/100))+Valor2
                            else: Valor3 = (Valor2*(37/100))+Valor2

                    S1=(0.5)
                    S2=(0.8)
                    S3=(0.3)
                    if Tipo==1:
                        if Estado==1:
                            S1= (S1+S2)
                        else:
                            S1= S1
                    else:
                        if Estado==1:
                            S1=(S1+S2+S3)
                        else:
                            S1=(S1+S3)
                            
                    Credito = S1*(12*Plazo)
                    Valor4=float(Credito+Valor3)
                    Dividendo=(Valor4/(12*Plazo))
                    print("Total del credito a pagar:",Valor4,"UF")
                    print("Dividendo mensual de:",round(Dividendo,2),"UF")
                               
                else:
                    print("Error:Estado de vivienda invalido")
            else:
                print("Error:Tipo de vivienda invalido")
        else:
            print("Error:Plazo invalido")
    else:
        print("Error:Pie fuera de rango")
else:
    print("Error:Valor fuera de rango")
