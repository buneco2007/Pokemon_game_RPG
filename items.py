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
            for item in self.items:
                print(item)
        else:
            print(f'Sua {self.nome} esta vazia!!!')


class MochilaPequena(Mochila):
    """Mochila_pequena Instancia uma mochila pequena

    Arguments:
        Mochila -- Herda da classe master mochila
    """
    nome = 'Mochila Pequena'
    espacos: int = 10


class Pokebola(object):
    """Pokebola Classe mestre de pokebola

    Arguments:
        object -- _description_
    """
