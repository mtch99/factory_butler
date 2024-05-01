from dataclasses import dataclass
from typing import List
import uuid

@dataclass
class Record:
    def __init__(self):
        self.__id__: str = str(uuid.uuid4())

    def __repr__(self):
        return f"Record(id={self.__id__})"

@dataclass
class Location:
    lon: float
    lat: float    
    name: str

    def __repr__(self):
        return f"Location(name={self.name}, lat={self.lat}, lon={self.lon})"

    def __str__(self):
        return f"{self.name} (Lat: {self.lat}, Lon: {self.lon})"

@dataclass
class Distributor(Record, Location):
    demand: int
    cost_of_shortage: float

    def __repr__(self):
        return (f"Distributor(name={self.name}, lat={self.lat}, lon={self.lon}, "
                f"demand={self.demand}, cost_of_shortage={self.cost_of_shortage})")

    def __str__(self):
        return (f"Distributor: {self.name}, Location: {self.lat}/{self.lon}\n"
                f"  Demand: {self.demand}, Cost of Shortage: ${self.cost_of_shortage}")

@dataclass
class Factory(Record, Location):
    capacity: int

    def __repr__(self):
        return (f"Factory(name={self.name}, lat={self.lat}, lon={self.lon}, "
                f"capacity={self.capacity})")

    def __str__(self):
        return f"Factory: {self.name}, Location: {self.lat}/{self.lon}, Capacity: {self.capacity}"

@dataclass
class Product(Record):
    name: str
    price: float

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}"

@dataclass
class Sale(Record):
    factory: str
    distributor: str
    quantity: int


    def __str__(self):
        return f"{self.factory} ----> {self.distributor}: {self.quantity} items \n"

@dataclass
class Distance(Record):
    value: float  # in km
    start_location: Location
    destination: Location

    def __repr__(self):
        return (f"Distance(value={self.value}, start={self.start_location.name}, "
                f"destination={self.destination.name})")

    def __str__(self):
        return f"Distance: {self.value} km from {self.start_location.name} to {self.destination.name}"


@dataclass
class Solution(Record):
    profit: float 
    sales: List[Sale]
    shortage: List[str] # List of distributors with shortage


    def __str__(self):
        return f"Solution: \n Profit: {self.profit} \n {self._stringify_sales()}"
    
    def _stringify_sales(self):
        result =  "--------- Sales: ----------- \n"
        for sale in self.sales:
            result += f"{sale}\n"

        result += "------------------------\n"
        return result
