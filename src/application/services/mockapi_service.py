import os
import httpx
from dotenv import load_dotenv


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

        url = f"{self.base_url}/contacts"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                return self.format_contacts(response.json())
            else:
                return None
