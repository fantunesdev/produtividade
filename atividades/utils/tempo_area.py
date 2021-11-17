class TempoArea():
    def __init__(self, nome, tempo, cor):
        self.__nome = nome
        self.__tempo = tempo
        self.__cor = cor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def tempo(self):
        return self.__tempo

    @tempo.setter
    def tempo(self, tempo):
        self.__tempo = tempo

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

### BUILDING LIST ###
# list = ['nome', 'tempo', 'cor']
