class Nodo(object):
    info,sig = None, None 

class datoPolinomio(object):

    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    def __init__(self):
        self.termino_may= None
        self.grado = -1
    
    def agregar_termino(polinomio,termino,valor):
        aux = Nodo()
        dato = datoPolinomio(valor,termino)
        aux.info = dato 
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while actual.sig is not None and termino < actual.info.termino:
                actual = actual.sig
                actual.sig = aux
    def modificar_termino(polinomio,termino,valor):
        aux = polinomio.termino_mayor
        while aux is not None and aux.info.termino != termino:
            aux = aux.sig
            aux.info.valor = valor           
