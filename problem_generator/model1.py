
from typing import List, Tuple
from uuid import uuid4
from problem.distribution_problem.model1 import Model1 as Model1Problem
from problem.distribution_problem.entities import Distance, Distributor, Factory, Product, Sale
from problem_generator import Generator
import random


class Model1(Generator):
    def __init__(
        self,
        delivery_fee_range: Tuple[int, int] = (100, 300),
        transportation_cost_range: Tuple[int, int] = (100, 200),
        price_range:Tuple[int, int] = (50, 500),
        demand_range: Tuple[int, int] = (10, 100),
        cost_of_shortage_range: Tuple[int, int] = (5, 50),
        quantity_range: Tuple[int, int] = (1, 20),
        distance_range: Tuple[int, int] = (1, 1000),
        num_products=5,
        num_factories=3,
        num_distributors=4
    ):
        self.__delivery_fee_range = delivery_fee_range
        self._transportation_cost_range = transportation_cost_range
        self.price_range = price_range
        self.demand_range = demand_range
        self.cost_of_shortage_range = cost_of_shortage_range
        self.quantity_range = quantity_range
        self.distance_range = distance_range
        self.num_products = num_products
        self.num_factories = num_factories
        self.num_distributors = num_distributors
        self._distance_list: List[Distance] = []
        self._product_list: List[Product] = []
        self._factory_list: List[Factory] = []
        self._distributor_list: List[Distributor] = []        

    
    def generate(self):
        transportation_cost = self.gen_transportation_cost()
        delivery_fee = self.gen_fixed_delivery_fee()
        self.__gen__product_list
        self.__gen_factory_list()
        self.__gen_distributor_list()
        self.__gen_distance_list__()
        problem = Model1Problem(
            fixed_delivery_fee=delivery_fee,
            transportation_cost=transportation_cost,
            products=self._product_list,
            factories=self._factory_list,
            distributors=self._distributor_list, 
            distances=self._distance_list
        )
        return problem


    def __gen_product(self, name=f"Product_{str(uuid4())}"):
        product =  Product(
            name,
            price=random.randint(*self.price_range)
        )
        return product
    
    def __gen__product_list(self):
        self._product_list = []
        for i in range(len(self._product_list)):
            product = self.__gen_product(name=f"Product_{len(self._product_list)+1}")
            self._product_list.append(product)
        return
    

    def __gen_factory(self):
        factory =  Factory(
            name=f"Factory_{len(self._factory_list)+1}",
            lon=random.uniform(-180, 180),
            lat=random.uniform(-90, 90)
        )
        return factory
    
    def __gen_factory_list(self):
        for i in range(self.num_factories):
            factory = self.__gen_factory()
            self._factory_list.append(factory)
        return

    def gen_distributor(self):
        distributor = Distributor(
            name=f"Distributor_{len(self._distributor_list)+1}",
            demand=random.randint(*self.demand_range),
            cost_of_shortage=random.randint(*self.cost_of_shortage_range)
        )
        return distributor
    
    def __gen_distributor_list(self):
        for i in range(len(self._distributor_list)):
            distributor = self.gen_distributor()
            self._distributor_list.append(distributor)
        return


    def __gen_distance__(self, start_location, end_location)->Distance:
        distance_value = random.randint(*self.distance_range)
        distance = Distance(distance_value,start_location, end_location)
        return distance


    def __gen_distance_list__(self):
        distance_list = [self.__gen_distance__(start_location, destination) for start_location in self._factory_list for destination in self._distributor_list]
        self._distance_list = distance_list
        return distance_list
    

    def gen_fixed_delivery_fee(self):
        delivery_fee = random.uniform(self.__delivery_fee_range[0], self.__delivery_fee_range[1]) 
        return delivery_fee

    def gen_transportation_cost(self):
        return random.uniform(self._transportation_cost_range[0], self._transportation_cost_range[1])