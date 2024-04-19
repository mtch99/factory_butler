from problem_generator.model1 import Model1 as Model1Generator
from solver.model1 import Solver_1
from problem_repository.model1 import get_last_problem, save_problem_to_json

generator = Model1Generator()
problem = get_last_problem() or generator.generate()


print(problem)
save_problem_to_json(problem)

solver = Solver_1()
solver.solve(problem)