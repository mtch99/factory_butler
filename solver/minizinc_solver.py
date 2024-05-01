
from typing import List
import numpy as np
import datetime
import copy

import enum
import os
import minizinc as mzn
from problem import solution
from problem.distribution_problem.DistributionProblem import Problem_1, Solution_1
from problem.distribution_problem.entities import Sale, Solution
from problem.problem import Problem
from solver import Solver


class MinizncSolver(Solver):


    def solve(self, prob=None):
        if(prob is None): return Solution_1([]) 
        if type(prob) is not Problem_1: raise TypeError('Le type du problème est invalide.')

        current_script_directory = os.path.dirname(os.path.realpath(__file__))
        model_file_path = os.path.join(current_script_directory, '..', 'minizinc', 'model.mzn')
        # model_file_path = os.path.realpath("../minizinc/model.mzn")
        model = mzn.Model(model_file_path)
        data_file_path = os.path.dirname(os.path.realpath(__file__)) + "/../minizinc/data.dzn"
        coinbc = mzn.Solver.lookup("coin-bc")
        instance = mzn.Instance(coinbc, model)
        # instance.add_file(data_file_path)
        # result = instance.solve()
        
        
        ## Set data
        self._set_enums(prob, instance)
        self._set_parameters(prob, instance)
        result = instance.solve()
        solution = self._parse_solution(result, prob)

        # if(mzn.Status.UNSATISFIABLE)

        # Retourner une solution
        return solution


    def _parse_solution(self, result: mzn.Result, problem: Problem_1):
        factories = problem.factories
        distributors = problem.distributors
        solution = result.solution
        profit = solution.objective
        sale_result_list: List[List[int]] = solution.Ventes
        sales = []
        for i, sale_result in enumerate(sale_result_list):
            factory_name = factories[i].name
            for j in range(len(sale_result)):
                distributor_name =  distributors[j].name
                qty = sale_result[j]
                sales.append(Sale(factory_name, distributor_name, qty))

        penurie_result_list = solution.Penurie
        shortage = []
        for penurie_result, i in enumerate(penurie_result_list):
            if(penurie_result == 1): shortage.append(distributors[i])
        return Solution(profit, sales, shortage)




    def _set_enums(self, problem: Problem_1, instance: mzn.Instance):
        usines = enum.Enum("Usine", [factory.name for factory in problem.factories])
        ditributeurs  = enum.Enum("Distributeur", [distributor.name for distributor in problem.distributors])
        instance["Usine"] = usines
        instance["Distributeur"] = ditributeurs
        return
    

    def _set_parameters(self, problem: Problem_1, instance: mzn.Instance):
        instance["demande"] = [distributor.demand for distributor in problem.distributors]
        instance["capacite"] = [factory.capacity for factory in problem.factories]
        instance["prix_vente"] = problem.product.price
        instance["cf_livraison"] = problem.fixed_delivery_fee
        instance["cv_transport"] = problem.transportation_cost
        instance["cf_penurie"] = [distributor.cost_of_shortage for distributor in problem.distributors]

        # Set the distances matrix between factories and distributors
        distance_matrix = [[0 for _ in range(len(problem.distributors))] for _ in instance["Usine"]]

        row = 0
        column = 0
        for distance in problem.distances:
            distance_matrix[row][column] = distance.value # type: ignore
            if(column == len(problem.distributors)-1):
                row+=1
                column=0
            else: 
                column+=1
        
        instance["distance"] = distance_matrix