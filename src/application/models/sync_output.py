from typing import List
from pydantic import BaseModel
from src.application.models.mailchimp_contact import MailchimpContact


class SyncOutput(BaseModel):
    synced_contacts: int
    contacts: List[MailchimpContact]
