import os
from src.infrastructure.clients.http_client import HttpClient


class MailchimpHttpClient():
    def __init__(self):
        self.client = HttpClient()

        self.base_url = os.getenv('MAILCHIMP_BASE_URL')
        if not self.base_url:
            raise ValueError('MAILCHIMP_BASE_URL is not set')

        self.api_key = os.getenv('MAILCHIMP_API_KEY')
        if not self.api_key:
            raise ValueError('MAILCHIMP_API_KEY is not set')

        self.client.set_url(self.base_url)
        self.client.set_headers({'Authorization': f'Bearer {self.api_key}'})

    async def get(self, endpoint):
        try:
            response = await self.client.get(endpoint=endpoint)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def post(self, endpoint, json):
        try:
            response = await self.client.post(endpoint=endpoint, json=json)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return None

    async def close(self):
        await self.client.close()
