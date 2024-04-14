from dataclasses import dataclass
from typing import List
from problem.distribution_problem.entities import Distance, Distributor, Factory, Product, Sale
from problem.problem import Problem


@dataclass
class Model1(Problem):
    fixed_delivery_fee: int
    transportation_cost: float # $/km
    products: List[Product]
    factories: List[Factory]
    distributors: List[Distributor]
    distances: List[Distance]
    sales: List[Sale]
    shortage: List[Distributor]
    profit: int