""" Modulo de items
    """


class Mochila(object):
    """Bag Classe master de mochila

    Arguments:
        object -- Objeto
    """

    def __init__(self, nome: str = 'Mochila', espacos: int = 5, items=None):
        self.nome = nome
        self.espacos = espacos
        if items is None:
            self.items: list = []

    def __str__(self) -> str:
        ocupado = len(self.items)
        return f'{self.nome} ({ocupado}/{self.espacos})'

    def add_item(self, item):
        """add_item Metodo para guardar item na mochila

        Arguments:
            item -- Item
        """
        if len(self.items) <= self.espacos:
            self.items.append(item)
        else:
            print(f'A {self.nome} nao tem espaco suficiente!!!')

    def mostrar_items(self):
        """mostrar_items Metodo para mostrar todos items da mochila
        """
        if self.items:
            print(f'Items na {self.nome}: ')
            for item in self.items:
                print(item)
        else:
            print(f'Sua {self.nome} esta vazia!!!')


class MochilaPequena(Mochila):
    """Mochila_pequena Instancia uma mochila pequena

    Arguments:
        Mochila -- Herda da classe master mochila
    """
    nome: str = 'Mochila Pequena'
    espacos: int = 10


class MochilaMedia(Mochila):
    """MochilaMedia Instancia uma mochila media

    Arguments:
        Mochila -- Herda da classe master mochila
    """
    nome = 'Mochila Media'
    espacos: int = 20


class MochilaGrande(Mochila):
    """MochilaGrande Instancia uma mochila grande

    Arguments:
        Mochila -- Herda da classe master mochila
    """
    nome = 'Mochila Grande'
    espacos = 40


class Pokebola():
    """Pokebola Classe mestre de pokebola

    Arguments:
        object -- Objeto
    """

    def __init__(self, nome: str = 'Pokebola', espacos: int = 1, item: list = None,
                 probabilidade: float = 1):
        self.nome = nome
        if espacos:
            self.espacos = espacos
        if item is None:
            self.item: list = []
        self.probabilidade = probabilidade

    def add_pokemon(self, pokemon):
        """add_pokemon Método para diconar pokemon na pokebola

        Arguments:
            pokemon -- Pokemon literalmente
        """
        if self.espacos < 1:
            return False
        else:
            self.item.append(pokemon)

    def remover_pokemon(self):
        """remover_pokemon Metodo para remover
        pokemon da pokebola
        """
        if self.item:
            self.item.clear()

    def __str__(self) -> str:
        return f'{self.nome}'


class PokebolaPremium(Pokebola):
    """PokebolaPremium Classe de pokebola premium

    Arguments:
        Pokebola -- Objeto
    """
    nome: str = 'Pokebola Premium'
    probabilidade: float = 100


class PokebolaMaster(Pokebola):
    """PokebolaPremium Classe de pokebola master

    Arguments:
        Pokebola -- Objeto
    """
    nome: str = 'Pokebola Master'
    probabilidade: float = 500
