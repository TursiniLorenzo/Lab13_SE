from dataclasses import dataclass

@dataclass
class Cromosoma :
    cromosoma : int

    def __str__ (self) :
        return f"Cromosoma : {self.cromosoma}"

    def __hash__ (self) :
        return hash (self.cromosoma)

