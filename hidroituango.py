#ENTRADA DEL PROBLEMA

nivelAgua=int(input("Digite el nivel de agua de la presa: "))

#PROCESO DEL PROBLEMA
if(nivelAgua >= 0 and nivelAgua < 20):
    print(f'El nivel de agua {nivelAgua} esta muy baja')
elif(nivelAgua >=20 and nivelAgua <400):    
    print(f'El nivel de agua {nivelAgua} es optimo')
elif(nivelAgua >=400 ):    
    print(f'El nivel de agua {nivelAgua} es peligroso')       
else:
    print(f'debe ingresar un rango mayor o igual a 20')                            











