from dataclasses import dataclass


@dataclass
class Irasas:
    suma: float


@dataclass
class PajamuIrasas(Irasas):
    siuntejas: str
    info: str


@dataclass
class IslaiduIrasas(Irasas):
    pirkinys: str
    info: str
