# Script creado el 07/04/2020 por Xabier Gabiña ak.Xabierland
# Mi Github: https://github.com/Xabierland
# Mi Twitter: https://twitter.com/Xabierland
# Mi Instagram: https://www.instagram.com/xabierland/

# Libreias importadas

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
    escribir(men1)

    

#Resetea en caso de que asi se desee para que se pueda introducir otra frase.
def reset():
    print("Escribe Y (Yes) para repetir o pulsa cualquier otra tecla para salir")
    select2=input()
    if select2=='Y' or select2=='y' or select2=="Yes" or select2=="yes":
        print("Introduce un nuevo mensaje por teclado")
        main()
    else:
        print("Abortando programa")
        exit

def escribir(men):
    men="".join(men)
    print("El mensaje resultante de la transformacion es:")
    print("=====================================================================================================================================================================")
    print (men)
    print("=====================================================================================================================================================================")

#Programa principal y encargado de llamar al resto de funciones
def main():
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
men=""
main()

#===========================================================================================================#
# Version 1.1
# Eres libre de editar y distribuir este codigo como te plazca sin necesidad de dar credito a mi, su autor.