""" Modulo principal do jogo
    """
from pokemon import PokemonAco
from pessoa import Player
from items import MochilaGrande, Pokebola


eu = Player('Fernando')
mochila = MochilaGrande()
pokebola = Pokebola()
pokemon = PokemonAco('Metal')

mochila.add_item(pokebola)
mochila.mostrar_items()
