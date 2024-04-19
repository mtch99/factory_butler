import math
import os
from typing import List
from requests import head
from amplpy import AMPL, Environment, add_to_path, DataFrame as ampl_df
import pandas as pd
import numpy as np

from problem.distribution_problem import Solution
from problem.distribution_problem.entities import Distance, Distributor, Factory, Product
from problem.distribution_problem.model1 import Problem_1 as Problem_1, Solution_1
from solver import Solver

# configure ampl instance
ampl_env = Environment('/Users/maximetchagou/Downloads/ampl_macos64')
ampl = AMPL(ampl_env)           
ampl.setOption('solver', 'gurobi')
ampl.setOption('gurobi_options', 'lim:time=2')
model_path = os.path.dirname(os.path.realpath(__file__)) + "/../ampl/model1.mod"


class Solver_1(Solver):
  
	def solve(self, problem: Problem_1) -> Solution:
		self._prepare()
		self._set_data(problem)
		ampl.solve()
		solution = self.parse_solution()
		return Solution([], 0)
  
	def _prepare(self):
		# ampl.reset()
		ampl.read(model_path)
		return


	def parse_solution(self):
		sales = ampl.get_variable("Ventes").get_values().to_dict()
		shortage = ampl.get_variable("Penurie").get_values().toDict()
		profit = ampl.get_objective("Profit").value()
		# print("S")
		return

	def _set_data(self, problem: Problem_1):
		self._set_factory_list(problem.factories)
		self._set_distributor_list(problem.distributors)
		self._set_distances(problem.distances)
		self._set_fixed_delivery_fee(problem.fixed_delivery_fee)
		self._set_transportation_cost(problem.transportation_cost)
		self._set_product_price(problem.product.price)
		return

	def _set_factory_list(self, factory_list: List[Factory]):
		# Create a pandas.DataFrame with data for n_min, n_max
		factory_df = pd.DataFrame(
			[
				(factory.name, factory.capacity) for factory in factory_list
			],
			columns=["Usine", "capacite"]
		).set_index("Usine")
		ampl.set_data(factory_df, "Usine")
		return
		  

	def _set_distributor_list(self, distributor_list: List[Distributor]):
		distributor_df = pd.DataFrame(
			[
				(distributor.name, distributor.demand, distributor.cost_of_shortage) for distributor in distributor_list
			],
			columns=["Distributeur", "demande", "cf_penurie"]
		).set_index("Distributeur")
		ampl.set_data(distributor_df, "Distributeur")
		return

	def _set_distances(self, distances: List[Distance]):
		ampl.param["distance"] = {
			(distance.start_location.name, distance.destination.name): distance.value 
			for distance in distances 
		}
		return
	
	def _set_fixed_delivery_fee(self, fixed_delivery_fee: float):
		ampl.param["cf_livraison"] = fixed_delivery_fee
		return
	
	def _set_transportation_cost(self, transportation_cost: float):
		ampl.param["cv_transport"] = transportation_cost
		return
	
	def _set_product_price(self, product_price: float):
		ampl.param["prix_vente"] = product_price
		return