#Ejercicio 1:
#Multiplicar 2 números sin usar el símbolo de la multiplicación

num1=5
num2=5
num3= 0

for i in range(num2):
    num3=num3+num1
print(num3)

#Ejercicio 2  Ingresar nombre y appelido e imprimelo al reves

nombre="ANTHONY"
reversed_String =''.join(reversed(nombre))
print(reversed_String)

#Ejercicio 3 crear una un script que encuentre el numero el elemnto menor a una lista 
lista=[9,1,2,3,4,8,6,7]

def menor (lista):
    min = lista[0]
    for x in lista:
        if x < min:
            min = x
            return min

def main(lista):
    print ("La lista es ", lista)    
    print ("El número menos es: ", min(lista))
 
main(lista)



#Ejercicio 5 Crear un scrip que indique si el usuario es mayor de edad
edad = 5

if edad>18 :
    print("Usted usuario es mayor de edad")
else:
         print("Usted usuario es menor de edad")    

#Ejercicio 6 Crear un scrip que me permita calcular si un numero es par o impar

num = 8
num2 = num % 2

if num2 == 0:
   print("Tu numero es par")
else:
    print("Tu numero es impar")    

# Ejercicio 7 Crear un scrip que indique cuantas vocales tiene un palabra

def contar_vocales(vocales):
    voc = 0
    for c in vocales:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            voc=voc+1
    return voc

vocales = "anthony"
print (contar_vocales(vocales))

#Ejercicio 8 Crear un script que reciba una cantidad infinita de numeros hasta decir basta, luego que imprima la suma de los numeros ingresadas,
ciclo = 2
num3 = 0
num2 = 0
while num2<ciclo:
    num2+=1
    num1 = 5   
    num3 = num1+num3 
    num4 = num3
    if num2>ciclo-1:
       print("La suma de tus numeros ingresados es igual:",num4)
   
#Ejercicio 9

cal=10

if cal>=9 and cal <= 10:
    print(f"{cal:} A")
elif cal>=8 and cal<9:
    print(f"{cal:} B")
elif cal>=7 and cal<8:
    print(f"{cal:} C")
elif cal>=6 and cal<7:
    print(f"{cal:} D")
elif cal>=0 and cal<6:
    print(f"{cal:} F")
else:
    print("Valor Desconocido")

#\n ejercisio 10        
numero=5
while numero >= 1:
    print(numero,end=",")
    numero=numero-1;


#\n ejercisio 11
numero4=0
while numero4 <=10:
    print(numero4,end=",")
    numero4=numero4+1;


#ejercisio 12

ancho=5
altura=10
area=ancho*altura
perimetro=altura+ancho
print("el area es",area)
print("el perimetro es",perimetro)

#ejercisio13
i=1
while i <=10:
    print(i,end=",")
    i=i+1
    if i==50:
        break
    i+=1

#ejercisio 14
libro="titanic"
autor="LEOARDO DICAPRO"
print(libro,autor)

#ejerciso 15
num1=int(input("Ingresa un numero -> "))
num2=int(input("Ingresa un numero -> "))
if num1 > num2 or num2 < num1:
    print(num1)
else:
    print(num2)

#ejercisio16
numeros ={13,1,8,3,2,5,8}
for numero in numeros:
    if numero > 5:
        break
    print(numeros)

#ejercisio17
num1=int(input("Ingresa un numero -> "))
print(num1**2)

#ejercisio18
num1=int(input("Ingresa un numero -> "))
num2=int(input("Ingresa un numero -> "))
print("la suma es",num1+num2)

#ejercisio19
numero = list(input("Ingresa un número de 5 cifras: -> "))
numero.reverse()

numero_al_reves = ''

for elemento in numero:
     numero_al_reves += elemento
     
print(numero_al_reves)
#ejercisio20
nombrepersona=(input("Ingresa tu nombre "))
print("hola como estas",nombrepersona)