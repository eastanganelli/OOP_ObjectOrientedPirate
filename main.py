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
                    if ship[2] is '' and ship[3] is '':
                        shipList.append(Ship(int(ship[0]), int(ship[1])))
                    elif ship[3] is '':
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
    pirate()