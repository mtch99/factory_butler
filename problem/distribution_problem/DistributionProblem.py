from dataclasses import dataclass
from typing import List
from problem.distribution_problem import DistributionProblem
from problem.distribution_problem.entities import Distance, Distributor, Factory, Product, Sale
from problem.problem import Problem


@dataclass
class Problem_1(DistributionProblem):
    fixed_delivery_fee: float
    transportation_cost: float # $/km
    product:  Product
    factories: List[Factory]
    distributors: List[Distributor]
    distances: List[Distance]
    

    def __repr__(self):
        output = f"Problem_1(fixed_delivery_fee={self.fixed_delivery_fee}, transportation_cost={self.transportation_cost}, product={self.product.name})\n"
        output += f"Factories: {[factory.name for factory in self.factories]}\n"
        output += f"Distributors: {[distributor.name for distributor in self.distributors]}\n"
        output += f"Distances: [{', '.join(f'{distance.start_location.name} to {distance.destination.name}: {distance.value}km' for distance in self.distances)}]"
        return output
    
    def __str__(self):
        output = f"Problem Overview:\n"
        output += f"  Product: {self.product.name}\n"
        output += f"  Delivery Fee: ${self.fixed_delivery_fee}\n"
        output += f"  Transportation Cost: ${self.transportation_cost}/km\n"
        output += "  Factories:\n    " + "\n    ".join(str(factory) for factory in self.factories) + "\n"
        output += "  Distributors:\n    " + "\n    ".join(str(distributor) for distributor in self.distributors) + "\n"
        output += "  Distances:\n    " + "\n    ".join(str(distance) for distance in self.distances) + "\n"
        return output

    

@dataclass
class Solution_1: 
    sales: List[Sale]