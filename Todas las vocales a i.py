# Script creado el 07/04/2020 por Xabier Gabiña ak.Xabierland
# Mi Github: https://github.com/Xabierland
# Mi Twitter: https://twitter.com/Xabierland
# Mi Instagram: https://www.instagram.com/xabierland/

# Libreias importadas
import keyboard
import time

#Todo lo que escriba se transforma en 'I'
def transforma(men):
    i=0
    men1= list(men)
    while i<=len(men1)-1:
        if men1[i]=='a' or men1[i]=='e' or men1[i]=='i' or men1[i]=='o' or men1[i]=='u':
            men1[i]='i'
        elif men1[i]=='A' or men1[i]=='E' or men1[i]=='I' or men1[i]=='O' or men1[i]=='U':
            men1[i]='I'
        
        i=i+1
    men1="".join(men1)
    print("El mensaje resultante de la transformacion es:")
    print (men1)

#Resetea en caso de que asi se desee para que se pueda introducir otra frase.
def reset():
    print("Pulsa ESC para salir o ENTER enter para continuar")
    reset=True
    while reset:
        if keyboard.is_pressed('enter'):
            reset=False
            print("Introduce un nuevo mensaje por teclado")
        else:
            print("Abortando programa") 
            
#Programa principal y encargado de llamar al resto de funciones
def main():
    men=""
    men=input()
    print(f"Tu mensaje a transformar es: =>  {men}  <= ?")
    print("Escribe Y/N (Yes/No) para continuar o pulsa cualquier otra tecla para salir")
    select1=input()
    if select1=='Y' or select1=='y' or select1=="Yes" or select1=="yes":
        transforma(men)
        reset()
    elif select1=='N' or select1=='n' or select1=="No" or select1=="no":
        print("Introduce el mensaje correcto por teclado")
        main()
    else:
        print("Abortando programa")

#Inicio       
print("Introduce un mensaje por teclado")
main()

#===========================================================================================================#
# Version 1.0
# Eres libre de editar y distribuir este codigo como te plazca sin necesidad de dar credito a mi, su autor.