import logging
from src.infrastructure.externals.mockapi_client import MockAPIClient


class GetContactsService:
    def __init__(self):
        self.client = MockAPIClient()

    async def execute(self):
        try:
            contacts = await self.client.get_contacts()
            await self.client.close()
            return contacts
        except Exception as e:
            logging.error(f'Error: {e}')
            await self.client.close()
            raise ConnectionError('Error getting contacts from MockAPI')
