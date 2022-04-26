texto=input("Inserte texto:")
significados=input("Inserte significados:")
emoji2=""
traduccion=""
flag_e=True
n=0
i=0
e=0
t=0
a=0
contador=0
significado2=""

for caracter in (significados):
    if caracter == "$":
        n+=1
while flag_e:
    if a<=n:
        while contador<= n:
            while e<= len(significados) and significados[e]!="*":
                e+=1
                emoji=(significados[i:e])
            while i <= len(significados) and significados[i]!="$":
                i+=1
                traducion=(significados[e+1:i]).upper()
            while t< len(texto):
                if emoji== texto[t:t+len(emoji)]:
                    traduccion+=traducion
                    t+=len(emoji)
                else:
                    traduccion+= texto[t]
                    t+=1
            
            contador+=1
        t=0
        e=len(emoji)+1
        i=len(traducion)+1
        a+=1
    else:
        flag_e=False



print(traduccion)
print(significado2 + emoji2)
#Hola <3, cómo estás? :-D
#<3*corazon$:-D*cara feliz$