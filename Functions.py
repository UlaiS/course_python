# def function(hello):
#     print(hello)


# def name(name):
#     print(name)


# def name(firstName, lastName):
#     print(firstName, lastName)


# def name(*names):
#     print(names)


def name(**kwargs):
    print(kwargs['nmobre'], kwargs['apellido'])


# function("funcion")
# name("Ulai Sem Nava Campos")
# name("Ulai Sem", "Nava Campos")
# name(firstName="Ulai Sem", lastName="Nava Campos")
# name(nombre="Ulai Sem", apellido="Nava Campos")

def concatNames(list):
    i = ''
    for name in list:
        i = i + ' ' + name
    return i


names = concatNames(["Ulai", "Sem", "Nava", "Campos"])
print(names)


def recursive(i):
    if i == 3:
        return i
    print(i)
    recursive(i+1)


recursive(0)