class Area():
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao