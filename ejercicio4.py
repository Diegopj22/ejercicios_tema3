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

    def obtener_valor(polinomio,termino):
       aux = polinomio.termino_mayor
       if aux is not None and aux.info.termino > termino:
            aux = aux.sig
       elif aux is not None and aux.info.termino == termino:
            return aux.info.valor
       else:
            return 0     

    def mostrar (polinomio):
       aux = polinomio.termino_mayor
       poli = ""
       signo = ""
       if aux.info.valor >= 0:
            singo += "+"
            pol += signo + str(aux.info.valor) + "x**" + str(aux.info.termino)       
       else:
        return poli
    
    def restar (polinomio1,polinomio2):
       paux = Polinomio()
       if polinomio1> polinomio2:
        mayor = polinomio1
       else:
        mayor = polinomio2
       for i in range(0, mayor.grado +1):
          total = polinomio1.obtener_valor(polinomio1, i) - polinomio2.obtener_valor(polinomio2, i)
          if total != 0:
            total.agregar_termino (paux, i , total)
            return paux