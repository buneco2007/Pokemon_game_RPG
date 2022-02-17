"""Modulo player
    """


class Pessoa(object):
    """Classe mestre de pessoa

    Args:
        object (_type_): _description_
    """

    def __init__(self, pokemons, nome: str = None):
        if nome:
            self.nome = nome
        else:
            self.nome = 'Desconhecido'
        self.pokemons = pokemons

    def __str__(self) -> str:
        return f'{self.nome}'
