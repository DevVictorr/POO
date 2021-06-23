from Animal import Animal


class cachorro(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def comer(self, racao):
        return super().comer(racao)

