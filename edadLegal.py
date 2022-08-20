

edad=int(input("Digite su edad:"))

if(edad <= 0 or edad >= 100):
    print()

if(edad >= 0 and edad <= 14):
    print(f'su edad es {edad}, es usted menor de edad')

elif(edad >=15 and edad <= 28):
    print(f'su edad es {edad}, es usted un joven')

elif(edad >=29 and edad <= 60):
    print(f'su edad es {edad}, es usted un adulto')
  





























