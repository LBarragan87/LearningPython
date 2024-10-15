def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x*10)
    return lista


def mi_generador():
    for x in range(1, 5):
        yield (x*10)


g = mi_generador()
print(mi_funcion())
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
