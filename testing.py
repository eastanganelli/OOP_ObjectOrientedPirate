import pytest
from src.ships import Ship, Cruise, Cargo


def is_cargo() -> None:
    listaCargos: list[int, float, int, int] = [
        [23, 0.25, 123, 45],
        [123, 1, 34, 34],
        [3, 0.5, 15, 65]
    ]
    
    for cargo in listaCargos:
        assert