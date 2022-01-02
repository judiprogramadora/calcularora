def suma(n1,n2):
    return (n1+ n2)
def resta (n1,n2):
    return (n1- n2)
def multiplicacion(n1,n2):
    return (n1* n2)
def division (n1,n2):
    if (n2== 0):
        return( "no se puede dividir entre 0")
    else:
        return (n1/ n2)    


print("ingrese que operacion")
print( "1- suma") 
print ("2- resta") 
print("3- multiplicacion")
print("4 - division") 
print("0- para salir")
    
opcion = int(input("eliga un opcion "))
while( opcion!=0):

    if (opcion==1):
        n1 =int (input ("ingrese 1 numero "))
        n2 = int (input ("ingrese otro numero ")) 
        print( suma(n1,n2))   
        opcion = int(input("eliga un opcion "))
    elif (opcion==2):
        n1 =int (input ("ingrese 1 numero "))
        n2 = int (input ("ingrese otro numero ")) 
        print( resta(n1,n2))
        opcion = int(input("eliga un opcion "))
    elif (opcion==3):
        n1 =int (input ("ingrese 1 numero "))
        n2 = int (input ("ingrese otro numero ")) 
        print( multiplicacion(n1,n2))
        opcion = int(input("eliga un opcion "))
    elif (opcion==4):
        n1 =int (input ("ingrese 1 numero "))
        n2 = int (input ("ingrese otro numero ")) 
        print( division(n1,n2))
        opcion = int(input("eliga un opcion "))
    else :
        print("opcion eqivocada ")      

