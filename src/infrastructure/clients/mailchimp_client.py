import os
from src.infrastructure.clients.httpx_client import HttpClient


class MailchimpClient():
    def __init__(self):
        self.client = HttpClient()
        self.base_url = os.getenv('MAILCHIMP_BASE_URL')
        self.api_key = os.getenv('MAILCHIMP_API_KEY')
        self.client.set_url(self.base_url)
        self.client.set_headers({'Authorization': f'Bearer {self.api_key}'})

    async def get(self, endpoint):
        try:
            response = await self.client.get(endpoint=endpoint)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def post(self, endpoint, json=None):
        try:
            response = await self.client.post(endpoint=endpoint, json=json)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def close(self):
        await self.client.close()
