from approval_demo.prettyworld import Person, Address, Family, City, find_related_people_in_same_cities
from approvaltests.approvals import verify


def test_approval():
    # ___ GIVEN ____
    # Creating City
    city = City(name='Sample City')

    # Creating some families
    alice = Person(name='Alice', age=25, address=Address(street='123 Street A', city=city))
    bob = Person(name='Bob', age=30, address=Address(street='456 Street B', city=city))
    family1 = Family(name='Smith', members=[alice, bob])

    charlie = Person(name='Charlie', age=28, address=Address(street='789 Street C', city=city))
    family2 = Family(name='Johnson', members=[charlie])

    alice.knows.append(charlie)

    # ___ WHEN ____
    related_people = find_related_people_in_same_cities([family1, family2])

    # ___ THEN ____
    verify(related_people)