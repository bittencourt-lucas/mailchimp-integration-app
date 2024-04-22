from pydantic import BaseModel


class Contact(BaseModel):
    email: str
    first_name: str
    last_name: str
