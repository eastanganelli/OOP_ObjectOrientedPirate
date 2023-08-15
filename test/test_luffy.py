import pytest
import csv
import requests
import codecs
from src.ships import Ship, Cargo, Cruise

def test_with_file():
    url="https://my.api.mockaroo.com/oop_pirate.csv?key=44ac9940"
    try:
        ShipLists = csv.reader(codecs.iterdecode(requests.get(url).iter_lines(), encoding="utf-8"), delimiter=",")
    except (requests.exceptions.ConnectionError, requests.exceptions.RequestException):
        ...
    else:
        myShips: list[any] = []
        header: bool = True
        for ship in ShipLists:
            if not header:
                try:
                    if ship[2] == '' and ship[3] == '':
                        myShips.append(Ship(int(ship[0]), int(ship[1])))
                    elif ship[3] == '':
                        myShips.append(Cruise(int(ship[2]), int(ship[0]), int(ship[1])))
                    else:
                        if ship[2] == '':
                            continue
                        myShips.append(Cargo(int(ship[2]), float(ship[3]), int(ship[0]), int(ship[1])))
                except ValueError:
                    continue
            else:
                header = False
        with pytest.raises(ValueError):
            for ship_ in myShips:
                assert (ship_.is_worth_it() >= 20) == True