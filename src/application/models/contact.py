from pydantic import BaseModel


class Contact(BaseModel):
    email: str
    firstName: str
    lastName: str
