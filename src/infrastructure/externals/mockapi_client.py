import os
from dotenv import load_dotenv
from src.infrastructure.clients.http_client import HttpClient


class MockAPIClient:
    def __init__(self):
        load_dotenv()

        self.base_url = os.getenv('MOCKAPI_BASE_URL')
        if not self.base_url:
            raise ValueError('MOCKAPI_BASE_URL is not set')

        self.client = HttpClient()
        self.client.set_url(self.base_url)
        self.client.set_headers({'Content-Type': 'application/json'})

    def format_contacts(self, contacts):
        return [
            {
                'firstName': contact['firstName'],
                'lastName': contact['lastName'],
                'email': contact['email']
            }
            for contact in contacts
        ]

    async def get_contacts(self):
        response = await self.client.get('/contacts')
        return self.format_contacts(response)

    async def close(self):
        await self.client.close()
