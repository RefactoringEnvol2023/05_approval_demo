from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta

from approvaltests import Options
from approvaltests.reporters.report_all_to_clipboard import copy_to_clipboard
from approvaltests.scrubbers.date_scrubber import DateScrubber

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

def test_with_date_scrubbers():
    # --Given--
    @dataclass
    class DatedNote:
        note: str
        date : datetime

        def merge(self, o: DatedNote):
            self.note = f'{self.note}/{o.note}'
            d = max(self.date, o.date)
            self.date =d

    now = datetime.now()
    later = now + timedelta(hours=2)
    dated_note0 = DatedNote("Foo", now)
    dated_note1 = DatedNote("Bar", later)

    def as_report(note: DatedNote):
        return f'NOTE:{note.note}, DATE={note.date.strftime("%Y%m%dT%H%M%SZ")}'

    # --When--
    dated_note1.merge(dated_note0)
    # --Then--
    verify(as_report(dated_note1),  options=Options().with_scrubber(DateScrubber.get_scrubber_for("00000000T000000Z")))