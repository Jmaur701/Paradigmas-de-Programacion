#=========================
# Jesus Mauricio Carrillo
#==============================
#   Paradigmas de programación.
#   Matematica Algoritmica 
#   ESFM-IPN Sept 2023
#====================================================
# Mi primera funcion 
#=====================================
def saludo()
#=======================================
 # Documentacion rapida de la funcion 
 #======================================
 """Esta funcion saluda"""
 print('!Quiúboles!, ¿Cómo estás?')

 #============================
 # Llamado de la funcion 
 #==============================
 saludo()

 #================================
 # Se ejecuta pero no se asigna
 #===============================
 salida=saludo()


#================================
# Esto NO funciona 
#================================
 print(salida)




#=======================
# MOstrar documentacion 
#=======================
# help(saludo)


#=============================
# Funcion con argumento 
#=============================
def salu2 (nombre):
    """Esta funcion saluda por tu nombre"""
    print(" Que onda ese", nombre, "!")
    salu2("Julian")
    salu2("Angel")

#=======================================
# Ahorrar trabajo del intérprete
# nombre:str la variable nombre es un str
#=======================================


def saludos(nombre:str):
    """ Esta funcion te saluda por tu nombre estrictamente"""
    print("!Que onda ese", nombre, "!")
    saludos("Julian")
   a = 123
   print(type(a))
   saludos(a)

#====================================
#Funcion con muchos argumentos 
#====================================
def saludos_multiples(nombre1, nombre2, nombre3:
        """Esta funcion saluda a 3 personas al mismo tiempo"""
        print("Hola", nombre1,",", nombre2, "y", nombre3)
saludos_multiples("Hugo", "Paco", "Luis")


#================================================
#Funcion con cualquier numero de argumentos
#================================================
def muchos_saludos(*nombres):
"""Esta funcion saluida a todos los que quieras"""
i =0 
#=====================================
# end = es para ponerlo de corrido 
#====================================
print ("Hola ", end="")
while len(nombres) > 1:
# Ultimo nombre
if ( i==len(nombres)-1):
    print(nombres[i])
    else:
    #Cualquier otro nombre
    print(nombres[i], end= ", ")
    i+=1
    # Video minuto 1:41
