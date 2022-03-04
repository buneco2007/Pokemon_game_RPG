""" Modulo para apresentacao de erros
    """
from typing import Type
from pokemon import Pokemon


class Erro:
    """Erro Classe que define os erros do jogo

    Arguments:
        object -- Object
    """

    def error_001(self, pokemon: Type[Pokemon]):
        """error_001 Erro de captura de pokemon

        Arguments:
            pokemon -- Pokemon que falhou em capturar
        """
        print(f'Falha ao capturar o pokemon {pokemon}')
