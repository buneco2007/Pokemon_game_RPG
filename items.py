""" Modulo de items
    """


from typing import Any


class Mochila(object):
    """Bag Classe master de mochila

    Arguments:
        object -- Objeto
    """

    def __init__(self, nome: str = 'Mochila', espacos: int = 1, items=None):
        self.nome = nome
        self.espacos = espacos
        if items is None:
            self.items: list = []

    def __str__(self) -> str:
        ocupado = len(self.items)
        return f'{self.nome} ({ocupado}/{self.espacos})'

    def add_item(self, item: Any) -> None:
        """add_item Metodo para guardar item na mochila

        Arguments:
            item -- Item
        """
        if len(self.items) <= self.espacos:
            self.items.append(item)
        else:
            print(f'A {self.nome} nao tem espaco suficiente!!!')

    def mostrar_items(self) -> None:
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

    def __init__(self):
        super().__init__(self)
        self.nome = 'Mochila Pequena'
        self.espacos = 5


class MochilaMedia(Mochila):
    """MochilaMedia Instancia uma mochila media

    Arguments:
        Mochila -- Herda da classe master mochila
    """

    def __init__(self):
        super().__init__(self)
        self.nome = 'Mochila Pequena'
        self.espacos = 15


class MochilaGrande(Mochila):
    """MochilaGrande Instancia uma mochila grande

    Arguments:
        Mochila -- Herda da classe master mochila
    """

    def __init__(self):
        super().__init__(self)
        self.nome = 'Mochila Pequena'
        self.espacos = 30


class Pokebola():
    """Pokebola Classe mestre de pokebola

    Arguments:
        object -- Objeto
    """

    def __init__(self, nome: str = 'Pokebola', espacos: int = 1, item: list = None,
                 probabilidade: float = 100):
        self.nome = nome
        if espacos:
            self.espacos = espacos
        if item is None:
            self.item: list = []
        self.probabilidade = probabilidade

    def __str__(self) -> str:
        return f'{self.nome}'

    def add_pokemon(self, pokemon: Any) -> None:
        """add_pokemon Método para diconar pokemon na pokebola

        Arguments:
            pokemon -- Pokemon literalmente
        """
        if self.espacos < 1:
            print(f'A pokebola ja tem o pokemon "{self.item[0]}" dentro!')
        else:
            self.item.append(pokemon)

    def remover_pokemon(self):
        """remover_pokemon Metodo para remover
        pokemon da pokebola
        """
        if self.item:
            self.item.clear()


class PokebolaPremium(Pokebola):
    """PokebolaPremium Classe de pokebola premium

    Arguments:
        Pokebola -- Objeto
    """

    def __init__(self):
        super().__init__(self)
        self.nome: str = 'Pokebola Premium'
        self.probabilidade: float = 100


class PokebolaMaster(Pokebola):
    """PokebolaPremium Classe de pokebola master

    Arguments:
        Pokebola -- Objeto
    """

    def __init__(self):
        super().__init__(self)
        self.nome: str = 'Pokebola Master'
        self.probabilidade: float = 500
