
import os
import json
import os
from dataclasses import dataclass, field, asdict, is_dataclass
from typing import List, Optional
from problem.distribution_problem.entities import Location
from problem.distribution_problem.model1 import Problem_1, Factory, Distributor, Product, Distance, Sale  # ensure all are imported

base_problem_path = os.path.dirname(os.path.realpath(__file__))
default_problem_filename = 'last_problem.json'

# Returns Problem_1 instance or None
def get_last_problem():
    default_problem_path = os.path.join(base_problem_path, default_problem_filename)
    if not os.path.exists(default_problem_path):
        print("No problem file found.")
        return None
    try:
        with open(default_problem_path, 'r') as file:
            data = json.load(file)
        return deserialize_problem(data)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except IOError as e:
        print(f"File read error: {e}")
        return None


def save_problem_to_json(problem:Problem_1, filename=default_problem_filename):
    filepath = os.path.join(base_problem_path, filename)
    try:
        with open(filepath, 'w') as f:
            json.dump(problem, f, cls=ComplexEncoder, indent=4)
        print(f"Problem saved successfully to {filepath}")
    except (IOError, TypeError) as e:
        print(f"Failed to save the problem: {e}")


def deserialize_problem(data):
    factories = [Factory(**f) for f in data['factories']]
    distributors = [Distributor(**d) for d in data['distributors']]
    distances = [
        Distance(
            value=dis['value'],
            start_location=Factory(**dis['start_location']),
            destination=Distributor(**dis['destination'])
        ) for dis in data['distances']
    ]
    product = Product(**data['product'])
    
    return Problem_1(
        fixed_delivery_fee=data['fixed_delivery_fee'],
        transportation_cost=data['transportation_cost'],
        product=product,
        factories=factories,
        distributors=distributors,
        distances=distances
    )



class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        return super().default(obj)