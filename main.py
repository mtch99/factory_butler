from problem_generator.model1 import Model1 as Model1Generator
from solver.model1 import Solver_1

generator = Model1Generator()
problem = generator.generate()

print(problem)

solver = Solver_1()
solver.solve(problem)