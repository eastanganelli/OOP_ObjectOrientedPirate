import pytest
from src.ships import Cruise
        
def test_is_Cruise() -> None:
    listaCruise: list[int, int, int] = [
        [23, 123, 45],
        [123, 34, 34],
        [78, 15, 65],
        [23, 30, 80]
    ]
    
    with pytest.raises(ValueError):
        for cruise in listaCruise:
            cruise: Cruise = Cruise(cruise[0], cruise[1], cruise[2])
            assert (cruise.is_worth_it() >= 20) == True