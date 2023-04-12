#Crear un directorio int.ospf.apellido1.apellido2 y un script de nombre int.ospf.apellido1.apellido2.py que contenga un menú con dos opciones de configuración, las cuales son: 

print("Seleccione alguna opción: \n 1. Configurar una interfaz. \n 2. Configurar una interfaz y configurar ospf.")
opcion=int(input("Ingrese opción uno o dos: "))

if opcion == 1:
    Interfaz=input("ingrese la interfaz que desea configurar (Ej: Fa0/0): ")
    IP=input("ingrese la dirección ip: ")
    Mascara=input("ingrese la mascara de subred: ")
    Nombre=input("ingrese el nombre de la interfaz: ")

    print("\nComandos para configurar la interfaz: ")
    print("\nInterface ",Interfaz )
    print(" no shutdown")
    print(" ip address ",IP, Mascara)
    print(" Description *",Nombre,"*")
    print(" Speed 100")
    print(" Duplex Full")
    print("\n\nConsulte con los siguientes comandos:")
    print("Show ip interface brief")
    print("Show run interface ",Nombre)
    print("Show interface",Interfaz)
    
else:
    Interfaz2=input("Ingrese la interfaz a configurar: ")
    ip2=input("Ingrese la dirección ip: ")
    Mascara2=input("ingrese la Máscara de subred: ")
    a=Mascara2.split(".")
    Nombre2=input("ingrese el nombre de la interfaz: ")
    proceso=input("ingrese el n° de proceso OSPF: ")
    IDospf=input("ingrese el ID del área OSPF: ")
    
    a1=str(255-int(a[0]))
    a2=str(255-int(a[1]))
    a3=str(255-int(a[2]))
    a4=str(255-int(a[3]))
    
    
    print("\nComandos para configurar la interfaz: ")
    print("\nInterface ",Interfaz2)
    print(" no shutdown")
    print(" ip address ",ip2,Mascara2)
    print(" Description *",Nombre2,"*")
    print(" Speed 100")
    print(" Duplex Full")
    print("\nRouter ospf ",proceso)
    print(" Network ", ip2,a1+"."+a2+"."+a3+"."+a4 )
    print(" Passive interface ",Interfaz2)
    print(" router-id",IDospf)
    print("\n\nConsulte con los siguientes comandos:\n")
    print("Show ip interface brief")
    print("Show run interface ",Nombre2)
    print("Show interface",Interfaz2)