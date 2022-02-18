"""Modulo player
    """


from typing import Any


class Pessoa(object):
    """Classe mestre de pessoa

    Args:
        object (_type_): _description_
    """

    def __init__(self, nome: str = None, pokemons=None):
        if nome:
            self.nome = nome
        else:
            self.nome = 'Desconhecido'
        if pokemons is None:
            self.pokemons = list[Any]

    def __str__(self) -> str:
        return f'{self.nome}'

    def capturar(self, pokemon):
        """capturar Funcao para capturar pokemon

        Arguments:
            pokemon -- Informar o pokemon
        """
        pass


class Player(Pessoa):
    """Player class

    Arguments:
        Pessoa -- Filho da classe
    """


class NPC(Pessoa):
    """NPC class

    Arguments:
        Pessoa -- Filho da classe
    """
