from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class Contact:
    first: Optional[str] = None
    last: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    _errors: frozenset = field(default_factory=frozenset)

    @property
    def errors(self):
        return dict(self._errors)

    def save(self) -> bool:
        with open("contacts.txt", "a") as contacts_file:
            try:
                print(
                    f"{self.first} {self.last} {self.phone} {self.email}",
                    file=contacts_file,
                )
            except:
                return False
            return True

    @staticmethod
    def search(query: str):
        all_contacts = Contact.all()
        all_contacts = [
            contact
            for contact in all_contacts
            if contact.first is not None and query in contact.first
        ]
        return all_contacts

    @staticmethod
    def all():
        with open("contacts.txt", "r") as contacts_file:
            lines = contacts_file.readlines()
            return {contact_from_file_line(line) for line in lines}


def contact_from_file_line(line: str) -> Contact:
    elems = line.split(" ")
    assert len(elems) == 4
    return Contact(first=elems[0], last=elems[1], phone=elems[2], email=elems[3])
