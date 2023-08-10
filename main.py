import csv
from src.ships import Ship, Cruise, Cargo

def read_pirate_notes() -> list[any]:
    shipList: list[any] = []
    
    try:
        with open("ships.csv", mode="r") as file:
            reader = csv.reader(file)
            header: bool = True
            for ship in reader:
                print(ship)
                if not header:    
                    if ship[2] == '' and ship[3] == '':
                        shipList.append(Ship(int(ship[0]), int(ship[1])))
                    elif ship[3] == '':
                        shipList.append(Cruise(int(ship[2]), int(ship[0]), int(ship[1])))
                    else:
                        shipList.append(Cargo(int(ship[2]), float(ship[3]), int(ship[0]), int(ship[1])))
                else:
                    header = False
                    
    except FileNotFoundError:
        exit("File Not found")
    else:
        return shipList
            
def pirate() -> None:
    shipList = read_pirate_notes()
    for ship in shipList:
        print(ship)

if __name__ == "__main__":
    # pirate()
    
    listaCargos: list[int, float, int, int] = [
        [23, 0.25, 123, 45],
        [123, 1, 34, 34],
        [78, 0.5, 15, 65],
        [2, 0.25, 34, 70]
    ]
    for cargo in listaCargos:
        print(cargo)
        try:
            cargo: Cargo = Cargo(cargo[0], cargo[1], cargo[2], cargo[3])
            print(cargo.is_worth_it())
        except ValueError:
            print("Not enough bounty")
    
    print("\nCruise Data")
    listaCruise: list[int, int, int] = [
        [23, 123, 45],
        [123, 34, 34],
        [78, 15, 65],
        [23, 30, 80]
    ]
    for cruise in listaCruise:
        print(cruise)
        try:
            cruise: Cruise = Cruise(cruise[0], cruise[1], cruise[2])
            print(cruise.is_worth_it())
        except ValueError:
            print("Not enough bounty")
    
    print("\nShip Data")
    listaShip: list[int, int] = [
        [23, 123],
        [123, 34],
        [78, 15],
        [23, 30]
    ]
    for ship in listaShip:
        print(ship)
        try:    
            ship: Ship = Ship(ship[0], ship[1])
            print(ship.is_worth_it())
        except ValueError:
            print("Not enough bounty")