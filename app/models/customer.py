from app.models.billing import Billing

class Customer:
    def __init__(self, id, email, firstname, lastname, sendOptInMail, billing):
        self.id = id
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.sendOptInMail = sendOptInMail
        self.billing = Billing(**billing) if billing else None

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "sendOptInMail": self.sendOptInMail,
            "billing": self.billing.__dict__ if self.billing else None
        }
