from enum import Enum


class SortOrder(Enum):
    ASC = 1
    DESC = 2


class Color(Enum):
    RED = 1
    FLORAL = 2
    GREEN = 3
    GREY = 4
    MULTICOLORED = 5
    WHITE = 6


class Collections(Enum):
    TSHIRT = 1
    DREAM_ANGELS = 2
    BODY_BY_VICTORIA = 3
    INCREDIBLE = 4
    LUXURY_LINGERIE = 5


class LingerieStyles(Enum):
    BABYDOLLS = 1
    CAMIS = 2
    CORSETS = 3
    DRESSES = 4
    ROBES = 5


class StalesOfPants(Enum):
    BIKINIES = 1
    BRIEFS = 2
    MULTI_PACK = 3
    SHAPEWEAR = 4
    THONGS = 5


class PantsSize(Enum):
    XS = 1
    S = 2
    M = 3
    M_L = 4
    L = 5
    XL = 6


class Fabrics(Enum):
    COTTON = 1
    NOSHOW = 2
    STEAMLESS = 3
    LACIE = 4


class StalesOfBras(Enum):
    SPORT = 1
    BALCONETTE = 2
    TOP = 3
    DEMI = 4
    CORSETS = 5


class CupsSize(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    G = 5
    G_PLUS = 6


class LiningLevel(Enum):
    LIGHTLY_LINED = 1
    PUSH_UP = 2
    UNLINED = 3
