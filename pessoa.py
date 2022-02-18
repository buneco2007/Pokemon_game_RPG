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
        else:
            self.pokemons = pokemons

    def __str__(self) -> str:
        return f'{self.nome}'

    def mostrar_pokemons(self):
        """mostrar_pokemons Funcao para mostrar os pokemons

        Returns:
            Lista com todos os pokemons
        """
        if self.pokemons:
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print('Voce nao tem nenhum pokemon')


class Player(Pessoa):
    """Player class

    Arguments:
        Pessoa -- Filho da classe
    """

    def capturar(self, pokemon):
        """capturar Funcao para capturar pokemon

        Arguments:
            pokemon -- Informar o pokemon
        """
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}!')


class NPC(Pessoa):
    """NPC class

    Arguments:
        Pessoa -- Filho da classe
    """
