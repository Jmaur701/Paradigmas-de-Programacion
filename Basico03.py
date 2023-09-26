#=============================
# Jesus Mauricio Carrillo
#==============================
#   Paradigmas de programación.
#   Matematica Algoritmica 
#   ESFM-IPN Sept 2023
#===================================================


#=========================
# Listas 
#Las listas pueden ser objetos diferentes
#=========================================
miprimeralista = [] # Es una lista vacia
print(miprimeralista)

#============================================
# Llenando lista
#=============================================
miprimeralista = [1 "Javier", 1.34, "Bosco", "Angel", "Abigail",True]
print(miṕrimeralista)

#========================================================================

# list; hacer una lista
# range(i,j): secuencia de 1 hasta j-1

#========================================================================
nums = list(range(1,61))

for i in nums:
        print(i)

#==================================================================
#incluir nuevos  elementos en la lista
#================================================================
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)
#================================================================
# quitar el elemento con indice 1
#==========================================================
i = 61
del nums[1]
print(nums)
#=========================================================
# Borrar la lista
#============================================================
del nums
#=================================================
# Sumar listas
#======================================
L1 =[1,2,3]
L2=[4,5,6]
print(L1+L2)

#=======================================================

# Llenado

#================================================================
potencial = []
for i int range(0, 10000):
        potencial.append(float(i))
        print(potencial[100])

#================================
#Generar una tupla con la lista
#=================================
potencial = tuple(potencial)
print(potencial[100]

