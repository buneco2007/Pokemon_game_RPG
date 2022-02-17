"""Modulo de tipos de pokemons
    """

import tipos


class Aco(tipos.Tipos):
    """Classe de pokemon aço

    Args:
        tipos (Str): Tipo do pokemon
    """
    tipo = tipos.Tipos.aco
    fraco: list[str] = [tipos.Tipos.aco, tipos.Tipos.agua, tipos.Tipos.eletrico,
                        tipos.Tipos.fogo]
    forte: list[str] = [tipos.Tipos.fada, tipos.Tipos.gelo,
                        tipos.Tipos.rocha]
    imune: list[str] = []


class Agua(tipos.Tipos):
    """Classe de pokemon de água

    Args:
        tipos (str): Tipo de pokemon
    """
    tipo: str = tipos.Tipos.agua
    fraco: list[str] = [tipos.Tipos.agua,
                        tipos.Tipos.dragao, tipos.Tipos.planta]
    forte: list[str] = [tipos.Tipos.fogo, tipos.Tipos.rocha, tipos.Tipos.terra]
    imune: list[str] = []


class Bicho(tipos.Tipos):
    """Classe de pokemon bicho

    Args:
        tipos (str): Tipo de pokemon
    """
    tipo: str = tipos.Tipos.bicho
    fraco: list[str] = [tipos.Tipos.aco, tipos.Tipos.fantasma, tipos.Tipos.fogo,
                        tipos.Tipos.fada, tipos.Tipos.luta, tipos.Tipos.veneno,
                        tipos.Tipos.voador]
    forte: list[str] = [tipos.Tipos.planta,
                        tipos.Tipos.psiquico, tipos.Tipos.sinistro]
    imune: list[str] = []


class Dragao(tipos.Tipos):
    """Classe de pokemon dragao

    Args:
        tipos (str): Tipo de pokemon
    """
    tipo: str = tipos.Tipos.dragao
    fraco: list[str] = [tipos.Tipos.aco]
    forte: list[str] = [tipos.Tipos.dragao]
    imune: list[str] = [tipos.Tipos.fada]
