class Circulo():
    pi = 3.14

    def __init__(self, raio = 5):
        self.raio = raio

    def area(self):
        print((self.raio * self.raio) * Circulo.pi)

    def setRaio(self, novoRaio):
        self.novoRaio = novoRaio
    
    def getRaio(self):
        print(self.novoRaio)
        
