from pydantic import BaseModel


class MailchimpContact(BaseModel):
    email_address: str
    status: str
    merge_fields: dict
