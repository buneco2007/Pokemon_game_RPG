"""Modulo de tipos de pokemons
    """

from typing import Any, List
import tipos


class Aco(tipos.Tipos):
    """Classe que pokemon do tipo aco
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
