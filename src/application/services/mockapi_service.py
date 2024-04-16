import os
from dotenv import load_dotenv
from src.infrastructure.clients.httpx_client import HttpxClient


class MockAPIService:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("MOCKAPI_BASE_URL")

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
        if not self.base_url:
            raise ValueError("MOCKAPI_BASE_URL is not set")
        client = HttpxClient()
        client.set_url(self.base_url)
        client.set_headers({'Content-Type': 'application/json'})
        response = await client.get('/contacts')
        await client.close()

        return self.format_contacts(response)
