from dataclasses import dataclass
import uuid

@dataclass
class Record: 
    def __init__(self):
        self.__id__: str = str(uuid.uuid4())


@dataclass
class Location:
    lon: float
    lat: float    


@dataclass
class Distributor(Record):
    name: str
    demand: int
    cost_of_shortage: float


@dataclass
class Factory(Record, Location): 
    name: str
    capacity: int


@dataclass
class Product(Record):
    name: str
    price: float


@dataclass
class Sale(Record):
    product: Product
    factory: Factory
    distributor: Distributor
    quantity: int

@dataclass
class Distance(Record):
    value: float # in km
    start_location: Location
    destination: Location

    