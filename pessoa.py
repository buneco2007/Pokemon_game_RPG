"""Modulo player
    """


from typing import Any


class Pessoa(object):
    """Classe mestre de pessoa

    Args:
        object (_type_): _description_
    """

    def __init__(self, nome: str = None, pokemons=None, items=None):
        if nome:
            self.nome = nome
        else:
            self.nome = 'Desconhecido'
        if pokemons is None:
            self.pokemons: list = []
        if items is None:
            self.items: list = []

    def __str__(self) -> str:
        return f'{self.nome}'


class Player(Pessoa):
    """Player class

    Arguments:
        Pessoa -- Filho da classe
    """

    def capturar(self, pokemon: Any, pokebola: Any) -> None:
        """capturar Funcao para capturar pokemon

        Arguments:
            pokemon -- Informar o pokemon
        """
        if pokemon.ser_capturado(pokebola):
            pokebola.add_item(pokemon)
            print(f'{self} capturou {pokemon}!')
        else:
            print(f'Falha em capturar o pokemon {pokemon}')

    def mostrar_items(self) -> None:
        """mostrar_items Metodo para mostrar todos os items
        """
        if self.items:
            print(f'Items em posse de {self}')
            for item in self.items:
                print(item)
        else:
            print(f'{self.nome} nao tem nenhum item em sua posse!!!')

    def add_item_mochila(self, item: Any, mochila: Any) -> None:
        """add_item_mochila Metodo para adicionar item na mochila

        Arguments:
            item -- _description_
        """
        mochila.add_item(item)
        print(f'{item} adicionado com sucesso na mochila!!!')

    def mostrar_pokemons(self) -> None:
        """mostrar_pokemons Funcao para mostrar os pokemons

        Returns:
            Lista com todos os pokemons
        """
        if self.pokemons:
            print(f'Pokemons de {self.nome}:')
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f'{self} nao tem nenhum pokemon!!!')


class NPC(Pessoa):
    """NPC class

    Arguments:
        Pessoa -- Filho da classe
    """
