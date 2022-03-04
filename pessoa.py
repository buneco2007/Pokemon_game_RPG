"""Modulo player
    """


from typing import Any
from items import Pokebola
from mensagens import Erro, Geral, Sucesso
from pokemon import Pokemon


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

    def capturar(self, pokemon: Pokemon, pokebola: Pokebola) -> None:
        """capturar Funcao para capturar pokemon

        Arguments:
            pokemon -- Informar o pokemon
        """
        if pokemon.ser_capturado(pokebola):
            pokebola.add_pokemon(pokemon)
            Sucesso.sucesso_001(self.nome, pokemon)
        else:
            Erro.error_001(pokemon)

    def mostrar_items(self) -> None:
        """mostrar_items Metodo para mostrar todos os items
        """
        if self.items:
            Geral.geral_001(self.nome)
            for item in self.items:
                print(item)
        else:
            print(f'{self.nome} nao tem nenhum item em sua posse!!!')

    def pegar_item(self, item: Any) -> None:
        """pegar_item Metodo para pegar um item

        Arguments:
            item -- Item qualquer
        """
        self.items.append(item)
        print(f'{self} pegou com sucesso {item}')

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
