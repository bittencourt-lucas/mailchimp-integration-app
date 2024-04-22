from typing import List
from pydantic import BaseModel
from src.application.models.contact import Contact


class SyncOutput(BaseModel):
    synced_contacts: int
    contacts: List[Contact]
