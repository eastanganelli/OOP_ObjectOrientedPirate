class Ship:
    __shipsCounter = 0
    
    def __init__(self, draft: int, crew: int) -> None:
        self._draft = draft
        self._crew = crew
        
        Ship.__shipsCounter += 1
        self.__id = f"Ship-{Ship.__shipsCounter}"
    
    def is_worth_it(self) -> int:
        value: int = self._draft - self._crew * 1.5
        if value > 20:
            return value
        raise ValueError
    
    def __str__(self) -> str:
        return f"{self.__id} - Cargo: {self._draft} - Crew: {self._crew} - "

class Cargo(Ship):
    def __init__(self, cargo: int, quality: float, draft: int, crew: int) -> None:
        super().__init__(draft, crew)
        self.__cargo = cargo
        self.__quality = quality
        
    def is_worth_it(self) -> int:
        addition: float = 3.5 if self.__quality == 1 else ( 2 if self.__quality == 0.5 else 0.5 )
        value: int = self._draft + self.__cargo * addition - self._crew * 1.5
        if value > 20:
            return value
        raise ValueError
    
    def __str__(self) -> str:
        return super().__str__() + f"Cargo: {self.__cargo} - Quality: {self.__quality}"

class Cruise(Ship):
    
    def __init__(self, passengers: int, draft: int, crew: int) -> None:
        super().__init__(draft, crew)
        self.__passengers = passengers
    
    def is_worth_it(self) -> int:
        value: int = self._draft + self.__passengers * 2.25 - self._crew * 1.5
        if value > 20:
            return value
        raise ValueError
    
    def __str__(self) -> str:
        return super().__str__() + f"Passengers: {self.__passengers}"
     
if __name__ == "__main__":
    pass