from src.infrastructure.externals.mockapi_client import MockAPIClient


class GetContactsService:
    def __init__(self):
        self.client = MockAPIClient()

    async def execute(self):
        contacts = await self.client.get_contacts()
        await self.client.close()
        return contacts
