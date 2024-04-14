from dataclasses import dataclass
from typing import List
from problem.distribution_problem import DistributionProblem
from problem.distribution_problem.entities import Distance, Distributor, Factory, Product, Sale
from problem.problem import Problem


@dataclass
class Model1(DistributionProblem):
    fixed_delivery_fee: float
    transportation_cost: float # $/km
    products: List[Product]
    factories: List[Factory]
    distributors: List[Distributor]
    distances: List[Distance]
    

    def __repr__(self):
        output = f""
        output += "\n ----- Problème ----- \n"
        output += f"\n ---- Coût de livraison: {self.fixed_delivery_fee}"
        output += f"\n ----- Coût de transport: {self.transportation_cost}\n"
        # output += f"{self.get_factories_str()}
        output += f"\n{self.get_factories_str()}\n"
        output += f""

        return output


    def get_factories_str(self):
        output = f"\n ------ Usines -------\n"
        for factory in self.factories:
            output += f"name: {factory.name} \n"
            output += f"localisation: {{latitude: {factory.lat}, longitude: {factory.lon}}}\n"
        return output
