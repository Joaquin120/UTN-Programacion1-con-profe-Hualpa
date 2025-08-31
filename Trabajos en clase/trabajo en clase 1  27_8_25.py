nombre=input("escribe tu nombre:")
apellido=input("escribe tu apellido:")
edad=int(input("ingrsa tu edad:"))
nivel_de_prioridad={
    "1":"emergencia",
    "2":"urgente",
    "3":"control"
}
obra_social=input("tenes obra social?")
prioridad_medica=int(input("ingresa el nivel de prioridad. 1 para emergencia,2 para urgente,3 para control:"))
if prioridad_medica==1:
    print (nivel_de_prioridad["1"])
    print ("asignar imediatamente a guardia")
elif prioridad_medica==2:
    print (nivel_de_prioridad["2"])
    if obra_social=="si":
        print ("turno en menos de 24 horas")
    elif obra_social=="no":
        print ("turno en 48 horas")
elif prioridad_medica==3:
    print (nivel_de_prioridad["3"])
    if edad>65:
        print ("turno preferencial en 72 horas")
    else:
        print ("turno normal en 7 días")    