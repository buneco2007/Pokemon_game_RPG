"""Modulo de tipos de pokemons
    """

from typing import Any, List
import tipos


class Aco(tipos.Tipos):
    """Classe de pokemon aço

    Args:
        tipos (Str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.aco
    normal: Any = [tipos.Tipos.bicho, tipos.Tipos.dragao, tipos.Tipos.fantasma,
                   tipos.Tipos.luta, tipos.Tipos.normal, tipos.Tipos.planta,
                   tipos.Tipos.psiquico, tipos.Tipos.sinistro, tipos.Tipos.terra,
                   tipos.Tipos.veneno, tipos.Tipos.voador]
    fraco: List = [tipos.Tipos.aco, tipos.Tipos.agua, tipos.Tipos.eletrico,
                   tipos.Tipos.fogo]
    forte: List = [tipos.Tipos.fada, tipos.Tipos.gelo,
                   tipos.Tipos.rocha]
    imune: List = []


class Agua(tipos.Tipos):
    """Classe de pokemon de água

    Args:
        tipos (str): Tipo de pokemon
    """
    tipo: str = tipos.Tipos.agua
    normal: Any = [tipos.Tipos.aco, tipos.Tipos.bicho, tipos.Tipos.eletrico,
                   tipos.Tipos.fantasma, tipos.Tipos.fada, tipos.Tipos.gelo,
                   tipos.Tipos.luta, tipos.Tipos.normal, tipos.Tipos.psiquico,
                   tipos.Tipos.sinistro, tipos.Tipos.veneno, tipos.Tipos.voador]
    fraco: list[str] = [tipos.Tipos.agua,
                        tipos.Tipos.dragao, tipos.Tipos.planta]
    forte: list[str] = [tipos.Tipos.fogo, tipos.Tipos.rocha, tipos.Tipos.rocha]
    imune: list[str] = []
