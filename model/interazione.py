from dataclasses import dataclass
from model.gene import Gene
from model.cromosoma import Cromosoma

@dataclass
class Interazione :
    gene1 : str
    gene2 : str
    cromosoma1 : int
    cromosoma2 : int
    correlazione : float

    def __str__ (self) :
        return f"{self.gene1} - {self.gene2} - {self.correlazione}"

    def __hash__ (self) :
        return hash ((self.gene1, self.gene2))