#=========================
# Jesus Mauricio Carrillo
#==============================
#   Paradigmas de programación.
#   Matematica Algoritmica 
#   ESFM-IPN Sept 2023
#=============================

''' Este es un super comentaerio de inicio a nuestro resumen
'''

#====================
# Operaciones basicas
#====================
 
 print (2+3)
 print (2*3)
 print (2/3)
 print (2**10)
 print (2**0.5) #raiz cuadrada
 print (10%2)
 print (10%0.1) #exclusivos en python

 #=========================================
 # Para saber el tipó de objeto se usa type
 #=========================================
 t=0
 print(type(t)) #entero
 t=3.6
 print(type(t)) #real flotante 
 t=True 
 print(type(t)) #booleano (bool)
 #======================
 # Mensajes a pantalla
 #======================
 print ("Este es un comando de python")
 print ('id: ', 1)
 print ('First Name; ', 'Steve')
 print ('Last Name: ', 'Jobs')
 print ("Vamos a sumar a esto" + " con esto otro ")
 #=============================================
 #Continuar una instruccion en varios renglones
 #=============================================
 if 100>99 and \
         200<= 300 and \
         True != False:
             print('Hello World!')
#==========================================================
# Comandos diferente en la misma linea 
#==========================================================
print ("Hola"); print ("Tu!!") # se considera mala practica
#=========================================================
# Usando parentesis, redondos cuadrados o llaves
# Se puede escribir en varios renglones
#==========================================================
list = [1, 2, 3, 4
        5, 6, 7, 8
        9, 10, 11, 12]
matriz = [ [1,2,3,4],[5, 6, 7, 8],[9,10,11,12]

print(list)
print(matriz)

#==================================================================
# Indentación estricta para procesos dependientes de : (dos puntos)
#==================================================================
if 10>5:
print ("Diez es mayor a cinco")
print ("Otra indentacion")
for i in list:
print (i)
print ("ok")
if 10>5:
    print("verdadero")
    elif 5>3: #Comienza segundo condicional 
    print ("Esto no se imprimira")
    else:
    print ("aqui nunca llega")

#==================
# Funciones 
#==================
def say_hello(name):
    print("Hello", name)
    print("Welcome to Python Tutorials")

say_hello("Julian")


