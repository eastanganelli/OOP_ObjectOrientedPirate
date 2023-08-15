import csv/
from src.ships import Ship, Cruise, Cargo

def read_pirate_notes() -> list[any]:
    shipList: list[any] = []
    
    with open("ships.csv", mode="r") as file:
        reader = csv.reader(file)
        header: bool = True
        for ship in reader:
            if not header:
                try:
                    if ship[2] == '' and ship[3] == '':
                        shipList.append(Ship(int(ship[0]), int(ship[1])))
                    elif ship[3] == '':
                        shipList.append(Cruise(int(ship[2]), int(ship[0]), int(ship[1])))
                    else:
                        if ship[2] == '':
                            continue
                        shipList.append(Cargo(int(ship[2]), float(ship[3]), int(ship[0]), int(ship[1])))
                except ValueError:
                    continue
            else:
                header = False        
        return shipList
            
def pirate() -> None:
    shipList = read_pirate_notes()
    for ship in shipList:
        print(ship)

if __name__ == "__main__":
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
        
        for ship_ in myShips:
            try:
                print(ship_.is_worth_it() >= 20)
            except ValueError:
                print("La carga no tiene valor")
    
    """try:
        ShipLists: any = read_pirate_notes()
    except FileNotFoundError:
        exit("No se encontró el archivo")
    else:
        for ship in ShipLists:
            try:
                print(ship)
                print(f"tiene un valor de {ship.is_worth_it()}")
            except ValueError:
                print("La carga no tiene valor")
            print("------------")"""