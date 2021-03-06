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


class Eletrico(tipos.Tipos):
    """Classe de pokemon eletrico

    Args:
        tipos (str): Tipo de pokemon
    """
    tipo: str = tipos.Tipos.eletrico
    fraco: list[str] = [tipos.Tipos.dragao, tipo, tipos.Tipos.planta]
    forte: list[str] = [tipos.Tipos.agua, tipos.Tipos.voador]
    imune: list[str] = [tipos.Tipos.terra]


class Fantasma(tipos.Tipos):
    """Classe de pokemon fantasma

    Args:
        tipos (str): Tipo de pokemon
    """
    tipo: str = tipos.Tipos.fantasma
    fraco: list[str] = [tipos.Tipos.sinistro]
    forte: list[str] = [tipo, tipos.Tipos.psiquico]
    imune: list[str] = [tipos.Tipos.normal]


class Fogo(tipos.Tipos):
    """Classe de pokemon fogo

    Args:
        tipos (str): Tipo de pokemon
    """
    tipo: str = tipos.Tipos.fogo
    fraco: list[str] = [tipos.Tipos.agua,
                        tipos.Tipos.dragao, tipo, tipos.Tipos.rocha]
    forte: list[str] = [tipos.Tipos.aco, tipos.Tipos.bicho,
                        tipos.Tipos.gelo, tipos.Tipos.planta, ]
    imune: list[str] = []


class Fada(tipos.Tipos):
    """Classe de pokemon fada

    Args:
        tipos (str): Tipo de pokemon
    """
    tipo: str = tipos.Tipos.fada
    fraco: list[str] = [tipos.Tipos.aco, tipos.Tipos.fogo, tipos.Tipos.veneno]
    forte: list[str] = [tipos.Tipos.dragao,
                        tipos.Tipos.luta, tipos.Tipos.sinistro]
    imune: list[str] = []


class Gelo(tipos.Tipos):
    """Classe de pokemon gelo

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.gelo
    fraco: list[str] = [tipos.Tipos.aco,
                        tipos.Tipos.agua, tipos.Tipos.fogo, tipo]
    forte: list[str] = [tipos.Tipos.dragao, tipos.Tipos.planta,
                        tipos.Tipos.terra, tipos.Tipos.voador]
    imune: list[str] = []


class Luta(tipos.Tipos):
    """Classe de pokemon luta

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.luta
    fraco: list[str] = [tipos.Tipos.bicho, tipos.Tipos.fada,
                        tipos.Tipos.psiquico, tipos.Tipos.veneno, tipos.Tipos.voador]
    forte: list[str] = [tipos.Tipos.aco, tipos.Tipos.gelo,
                        tipos.Tipos.normal, tipos.Tipos.rocha, tipos.Tipos.sinistro]
    imune: list[str] = [tipos.Tipos.fantasma]


class Normal(tipos.Tipos):
    """Classe de pokemon luta

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.normal
    fraco: list[str] = [tipos.Tipos.aco, tipos.Tipos.rocha]
    forte: list[str] = []
    imune: list[str] = [tipos.Tipos.fantasma]


class Planta(tipos.Tipos):
    """Classe de pokemon planta

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.planta
    fraco: list[str] = [tipos.Tipos.aco, tipos.Tipos.bicho, tipos.Tipos.dragao,
                        tipos.Tipos.fogo, tipo, tipos.Tipos.veneno, tipos.Tipos.voador]
    forte: list[str] = [tipos.Tipos.agua, tipos.Tipos.rocha, tipos.Tipos.terra]
    imune: list[str] = []


class Psiquico(tipos.Tipos):
    """Classe de pokemon psiquico

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.psiquico
    fraco: list[str] = [tipos.Tipos.aco, tipo]
    forte: list[str] = [tipos.Tipos.luta, tipos.Tipos.veneno]
    imune: list[str] = [tipos.Tipos.sinistro]


class Rocha(tipos.Tipos):
    """Classe de pokemon psiquico

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.psiquico
    fraco: list[str] = [tipos.Tipos.aco, tipos.Tipos.luta, tipos.Tipos.terra]
    forte: list[str] = [tipos.Tipos.bicho, tipos.Tipos.fogo,
                        tipos.Tipos.gelo, tipos.Tipos.voador]
    imune: list[str] = []


class Sinistro(tipos.Tipos):
    """Classe de pokemon psiquico

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.psiquico
    fraco: list[str] = [tipos.Tipos.fada, tipos.Tipos.normal, tipo]
    forte: list[str] = [tipos.Tipos.fantasma, tipos.Tipos.psiquico]
    imune: list[str] = []


class Terra(tipos.Tipos):
    """Classe de pokemon psiquico

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.psiquico
    fraco: list[str] = [tipos.Tipos.bicho, tipos.Tipos.planta]
    forte: list[str] = [tipos.Tipos.aco, tipos.Tipos.eletrico, tipos.Tipos.fogo,
                        tipos.Tipos.rocha, tipos.Tipos.veneno]
    imune: list[str] = [tipos.Tipos.voador]


class Veneno(tipos.Tipos):
    """Classe de pokemon psiquico

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.psiquico
    fraco: list[str] = [tipos.Tipos.fantasma,
                        tipos.Tipos.rocha, tipos.Tipos.terra, tipo]
    forte: list[str] = [tipos.Tipos.fada, tipos.Tipos.planta]
    imune: list[str] = [tipos.Tipos.aco]


class Voador(tipos.Tipos):
    """Classe de pokemon psiquico

    Args:
        tipos (str): Tipo do pokemon
    """
    tipo: str = tipos.Tipos.psiquico
    fraco: list[str] = [tipos.Tipos.aco,
                        tipos.Tipos.eletrico, tipos.Tipos.rocha]
    forte: list[str] = [tipos.Tipos.bicho,
                        tipos.Tipos.luta, tipos.Tipos.planta]
    imune: list[str] = []
