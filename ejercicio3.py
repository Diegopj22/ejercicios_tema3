class Nave:
    def __init__(self,nombre,largo,trip,cant_pas):
        self.nombre= nombre
        self.largo= largo
        self.trip= trip
        self.cant_pas= cant_pas
    
    def __str__(self):
        info ="Nave:"+ self.nombre
        info += ",largo"+ str(self.largo)
        info += ",tripulación:" + str(self.trip)
        info += ",cantidad de pasajeros:" + str(self.trip)
        return info 
        
        