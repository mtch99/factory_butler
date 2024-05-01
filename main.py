from problem.distribution_problem.DistributionProblem import Problem_1
from problem_generator.model1 import Model1 as Model1Generator
from solver.minizinc_solver import MinizncSolver
from solver.model1 import Solver_1
from problem_repository.model1 import get_problem, save_problem_to_json
import sys


generator = Model1Generator()

problem: Problem_1
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    problem = get_problem(file_path) or generator.generate()
else:
    problem = get_problem() or generator.generate()
    


print(problem)
save_problem_to_json(problem)

solver = Solver_1()
solution = solver.solve(problem)
print(solution)


minizinc_solver = MinizncSolver()
minizinc_solution = minizinc_solver.solve(problem)
print(f"Solution minizinc {minizinc_solution}")