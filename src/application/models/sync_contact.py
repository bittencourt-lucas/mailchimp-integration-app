from pydantic import BaseModel


class SyncContact(BaseModel):
    email_address: str
    status: str
    merge_fields: dict
