class Livro():

    def __init__(self, nome, autor, paginas) :
        
        self.nome = nome
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return('O nome do livro é %s do autor %s com a quantidade de paginas sendo: %s' %(self.nome,self.autor,self.paginas))

    def __len__(self):
        return self.paginas