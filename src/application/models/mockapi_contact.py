from pydantic import BaseModel


class MockAPIContact(BaseModel):
    createdAt: str
    firstName: str
    lastName: str
    email: str
    avatar: str
    id: str
