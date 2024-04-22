import httpx
import logging
from httpx import Response


class HttpClient:
    def __init__(self):
        self.client = httpx.AsyncClient()

    def set_headers(self, headers: dict):
        self.headers = headers

    def set_url(self, url: str):
        self.url = url

    async def get(self, endpoint: str) -> dict:
        """
        Send a GET request to the specified endpoint.

        Returns the response as JSON if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        try:
            response: Response = await self.client.get(
                f'{self.url}{endpoint}',
                headers=self.headers
                )
            return response.json()
        except Exception as e:
            logging.error(f'Error: {e}')
            raise ConnectionError('Error with GET request on HTTP Client')

    async def post(self, endpoint: str, json: dict) -> dict:
        """
        Send a POST request to the specified endpoint.

        Returns the response as JSON if successful.
        Logs error and raises ConnectionError if an exception occurs.
        """
        try:
            response: Response = await self.client.post(
                f'{self.url}{endpoint}',
                headers=self.headers,
                json=json
                )
            return response.json()
        except Exception as e:
            logging.error(f'Error: {e}')
            raise ConnectionError('Error with POST request on HTTP Client')

    async def close(self):
        """
        Close the HTTP client.
        """
        await self.client.aclose()
