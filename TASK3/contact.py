class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def as_dict(self):
        return dict(name=self.name, phone=self.phone, email=self.email, address=self.address)

    # Keep update, summary, detail methods as before
