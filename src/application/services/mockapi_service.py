import os
import httpx
from dotenv import load_dotenv


class MockAPIService:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("MOCKAPI_BASE_URL")

    async def get_contacts(self):
        if not self.base_url:
            raise ValueError("MOCKAPI_BASE_URL is not set")

        url = f"{self.base_url}/contacts"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return None
