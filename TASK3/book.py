import json
from contact import Contact

class ContactBook:
    def __init__(self, file_path='contacts.json'):
        self.file_path = file_path
        self.contacts = []
        self.load()

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump([c.as_dict() for c in self.contacts], f, indent=2)

    def load(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            self.contacts = [Contact(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append(Contact(name, phone, email, address))
        self.save()

    def list_contacts(self):
        return self.contacts

    def search(self, keyword):
        key = keyword.lower()
        return [c for c in self.contacts if key in c.name.lower() or key in c.phone]

    def update_contact(self, idx, **kwargs):
        self.contacts[idx].update(**kwargs)
        self.save()

    def delete_contact(self, idx):
        del self.contacts[idx]
        self.save()
