class Atividade():
    def __init__(self, data, area, sub_area, plataforma, pessoa, descricao, detalhamento, tempo, inicio, fim, usuario):
        self.__data = data
        self.__area = area
        self.__sub_area = sub_area
        self.__plataforma = plataforma
        self.__pessoa = pessoa
        self.__descricao = descricao
        self.__detalhamento = detalhamento
        self.__tempo = tempo
        self.__inicio = inicio
        self.__fim = fim
        self.__usuario = usuario

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    @property
    def sub_area(self):
        return self.__sub_area

    @sub_area.setter
    def sub_area(self, sub_area):
        self.__sub_area = sub_area

    @property
    def plataforma(self):
        return self.__plataforma

    @plataforma.setter
    def plataforma(self, plataforma):
        self.__plataforma = plataforma

    @property
    def pessoa(self):
        return self.__pessoa

    @pessoa.setter
    def pessoa(self, pessoa):
        self.__pessoa = pessoa

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def detalhamento(self):
        return self.__detalhamento

    @detalhamento.setter
    def detalhamento(self, detalhamento):
        self.__detalhamento = detalhamento

    @property
    def tempo(self):
        return self.__tempo

    @tempo.setter
    def tempo(self, tempo):
        self.__tempo = tempo

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

### BUILDING LIST ###
# list = ['data', 'area', 'sub_area', 'plataforma', 'pessoa', 'descricao', 'detalhamento', 'tempo', 'inicio', 'fim', 'usuario']

class Area():
    def __init__(self, conhecimento, empreendedorismo, saude, financas, tecnologia, musica, tempo_total, contagem):
        self.__conhecimento = conhecimento
        self.__empreendedorismo = empreendedorismo
        self.__saude = saude
        self.__financas = financas
        self.__tecnologia = tecnologia
        self.__musica = musica
        self.__tempo_total = tempo_total
        self.__contagem = contagem

    @property
    def conhecimento(self):
        return self.__conhecimento

    @conhecimento.setter
    def conhecimento(self, conhecimento):
        self.__conhecimento = conhecimento

    @property
    def empreendedorismo(self):
        return self.__empreendedorismo

    @empreendedorismo.setter
    def empreendedorismo(self, empreendedorismo):
        self.__empreendedorismo = empreendedorismo

    @property
    def saude(self):
        return self.__saude

    @saude.setter
    def saude(self, saude):
        self.__saude = saude

    @property
    def financas(self):
        return self.__financas

    @financas.setter
    def financas(self, financas):
        self.__financas = financas

    @property
    def tecnologia(self):
        return self.__tecnologia

    @tecnologia.setter
    def tecnologia(self, tecnologia):
        self.__tecnologia = tecnologia

    @property
    def musica(self):
        return self.__musica

    @musica.setter
    def musica(self, musica):
        self.__musica = musica

    @property
    def tempo_total(self):
        return self.__tempo_total

    @tempo_total.setter
    def tempo_total(self, tempo_total):
        self.__tempo_total = tempo_total

    @property
    def contagem(self):
        return self.__contagem

    @contagem.setter
    def contagem(self, contagem):
        self.__contagem = contagem
