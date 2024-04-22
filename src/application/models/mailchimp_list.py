from pydantic import BaseModel


class MailchimpList(BaseModel):
    id: str
    name: str
