texto=input("Inserte texto:")
significados=input("Inserte significados:")

emoji=""
significado2=""
traduccion=""
flag_e=True
n=0
i=0
e=0
t=0
contador=0
traducion=" "

while flag_e:
    while e<= len(significados) and significados[e]!="*":
            e+=1
            emoji=(significados[i:e])
            e=0
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

print(traduccion)
#Hola <3, cómo estás? :-D
#<3*corazon$:-D*cara feliz$