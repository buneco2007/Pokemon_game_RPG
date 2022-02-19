""" Modulo de items
    """


class Mochila(object):
    """Bag Classe master de mochila

    Arguments:
        object -- Objeto
    """

    def __init__(self, nome: str = 'Mochila', espacos: int = 5,
                 items=None):
        self.nome = nome
        self.espacos = espacos
        if items is None:
            self.items = []
        else:
            self.items = items

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
    nome: str = 'Mochila Media'
    espacos: int = 20


class MochilaGrande(Mochila):
    """MochilaGrande Intancia uma mochila grande

    Arguments:
        Mochila -- herda da classe master mochila
    """
    nome: str = 'Mochila Grande'
    espacos: int = 40


class Pokebola(object):
    """Pokebola Classe mestre de pokebola

    Arguments:
        object -- Objeto
    """

    def __init__(self, espacos: int = 1, item: None = None):
        if espacos:
            self.espacos = espacos
        if item is None:
            self.item: list = []
