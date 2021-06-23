class Animal():

    def __init__(self,nome,idade) :
        self.nome = nome
        self.idade = idade

    def comer(self, racao):
        self.racao = racao

    def info(self):
        print("Nome do cachorro: " + self.nome + "\n idade do cachorro : " + self.idade + " \n Racao: " + self.racao)