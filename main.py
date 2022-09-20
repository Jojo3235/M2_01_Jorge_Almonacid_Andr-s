#1ª parte del ejercicio
print(type(3))          #Imprimimos el tipo del número 3(número entero)
print(type(2.3))        #Imprimimos el tipo del número 2.3(número flotante)
print(type("Hola"))     #Imprimimos el tipo de la palabra "Hola"(string)
print(type(0==1))       #Imprimimos el tipo del elemento 0==1(booleano)

#2ª parte del ejercicio
nombre="Jorge"                  #Creamos una variable con el nombre
apellido="Almonacid"            #Creamos otra variable con el apellido
print(nombre + apellido)        #Imprimimos ambas variables
print(nombre + apellido + ".")  #Imprimimos ambas variables con un punto al final
print(nombre*3)                 #Imprimimos el nombre 3 veces

#3ª parte del ejercicio
nombreCompleto = nombre + " " + apellido    #Creamos una variable con las 2 variables previamente definidas y añadimos un espacio en medio
print(nombreCompleto)                       #Imprimimos la variable con el nombre, apellido y un espacio en medio
print(nombreCompleto[slice(0,5)])           #Cortamos la variable desde 0 a 5(excluido) y imprimimos