import logging
from typing import List
from src.application.models.mockapi_contact import MockAPIContact
from src.infrastructure.externals.mockapi_client import MockAPIClient


class GetContactsService:
    def __init__(self):
        self.client = MockAPIClient()

    async def execute(self) -> List[MockAPIContact]:
        """
        Retrieve all contacts from MockAPI.

        Returns the contacts if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        try:
            contacts: List[MockAPIContact] = await self.client.get_contacts()
            await self.client.close()
            return contacts
        except Exception as e:
            logging.error(f'Error: {e}')
            await self.client.close()
            raise ConnectionError('Error getting contacts from MockAPI')
