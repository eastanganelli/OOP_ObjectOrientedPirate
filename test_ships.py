import pytest
from src.ships import Ship

def test_is_ship() -> None:
    listaShip: list[int, int] = [
        [23, 123],
        [123, 34],
        [78, 15],
        [23, 30]
    ]
    
    with pytest.raises(ValueError):
        for ship in listaShip:
            ship: Ship = Ship(ship[0], ship[1])
            assert (ship.is_worth_it() >= 20) == True 