""" Modulo principal do jogo
    """
from pokemon import PokemonAco
from pessoa import Player
from items import MochilaGrande


eu = Player('Fernando')
mochila = MochilaGrande()
pokemon = PokemonAco('Metal')

mochila.mostrar_items()
