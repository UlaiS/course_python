# #Este es mi primer if en python
#
# x = 5
# y = 3
# a, b, c = 55, 10, 8
# message = 'es mayor'
# hello = 'hola'
# mundo = 'mundo'
#
# q = w = e = r = t = 'QWERTY'
#
# # if x > y:
# #     print(message)
# # else:
# #     print('3 No es mayor que 5')
#
#
# # print(2/1) #FLOAT
# # print(2//1) #INTEGER
# # print(1j) #COMPLEJO
# # print(a,b,c)
# # print(q, w, e, r, t)
# # print(hello + ' ' + mundo)
#
# lista = ["Ulai","Sem","Nava","Campos"]
# lista2 = lista.copy()
# lista.append("Hijo")
# # print(lista)
# # print(lista, lista2.count("Ulai"))
# # print(len(lista), len(lista2))
# # Elimina el elemento según el valor ingresado como parametro
# # lista.remove("Ulai")
# # print(lista[0])
# # Eliminar el ultimo elemento
# # lista.pop()
# # print(lista)
# lista.sort()
# # print(lista)
# lista.reverse()
# # print(lista)
#
# tupla = ("Ulai","Sem","Nava","Campos")
# tuplaList = list(tupla)
# # print(tupla,"Tupla")
# # print(tupla.index("Nava"))
# # print(tupla.count("Ulai"))
# # print(tuplaList)
# rango = range(6)
# # print(rango)
#
# #####################################################
#
# # Ejemplo 1 de diccionario de datos
#
# diccionario = {
#     "nombre": "Ulai",
#     "apellido": "Nava",
#     "Edad": 27
# }
# # print(diccionario)
# # print(diccionario['nombre'])
# # print(diccionario.get('nombre'))
# diccionario['nombre'] = "Elelulai"
# # print(diccionario)
# # print(len(diccionario))
#
# diccionario['artista'] = 'si'
# diccionarioCopy = diccionario.copy()
# diccionarioCopyDict = dict(diccionario)
# # print(diccionario)
# diccionario.pop('artista')
# # print(diccionario)
# diccionario.popitem()
# # print(diccionario)
# del diccionario['apellido']
# # print(diccionario, diccionarioCopy, diccionarioCopyDict)
# # print(diccionario.clear())
#
#
#  # Ejemplo 2 de diccionario
# persona = {
#     "ulai": {
#         "apellido": "Nava",
#         "Edad": 27
#     },
#     "natali": {
#         "apellido": "Soto",
#         "Edad": 29
#     }
# }
# # print(persona)
#
# # Ejemplo 3 de diccionario de datos
# ulai = {
#         "apellido": "Nava",
#         "Edad": 27
#     }
#
# natali = {
#             "apellido": "Soto",
#             "Edad": 29
#     }
# dante = dict(nombre="dante")
# persona = {"ulai" : ulai, "natali": natali}
# # print(persona)
# # print(dante)
#
# #####################################################
#
# # boolean = True
# # print(boolean)
# # boolean = False
# # print(boolean)
# boolean = True if  x > y  else False
#
#
# dato = input("Ingresa nombre")
#
# print("no existe nombre ") if(lista[0] == dato) else print("oki")

i = 0
while(i < 7):
    i += 1
    if i == 5:
        continue
    print(i)

lista = ["Ulai", "Sem", "Nava", "Campos"]

for name in lista:
    print(name)