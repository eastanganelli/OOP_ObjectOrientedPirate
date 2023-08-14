import pytest
from src.ships import Cargo


def test_is_cargo() -> None:
    listaCargos: list[int, float, int, int] = [
        [23, 0.25, 123, 45, ],
        [123, 1, 34, 34],
        [78, 0.5, 15, 65],
        [2, 0.25, 34, 70]
    ]
    
    with pytest.raises(ValueError): 
        for cargo in listaCargos:
            cargo: Cargo = Cargo(cargo[0], cargo[1], cargo[2], cargo[3])
            assert (cargo.is_worth_it() >= 20) == True