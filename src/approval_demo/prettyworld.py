from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class City:
    name: str


@dataclass
class Address:
    street: str
    city: City


@dataclass
class Person:
    name: str
    age: int
    address: Optional[Address] = None
    knows: List[Person] = field(default_factory=list)


@dataclass
class Family:
    name: str
    members: List[Person] = field(default_factory=list)


def find_related_people_in_same_cities(families: List[Family]):
    people_relations_by_cities = {}
    for family in families:
        for people in family.members:
            if people.knows:
                city_name = people.address.city.name
                relations = people_relations_by_cities.get(city_name)
                if not relations:
                    relations = []
                    people_relations_by_cities[city_name] = relations
                relations.append(people)
    return people_relations_by_cities
